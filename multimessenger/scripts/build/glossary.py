from PyOrgMode import PyOrgMode
import sys
import orgparse

import string
class PartialFormatter(string.Formatter):
    def __init__(self, missing='', bad_fmt='!!'):
        self.missing, self.bad_fmt=missing, bad_fmt

    def get_field(self, field_name, args, kwargs):
        # Handle a key not found
        try:
            val=super(PartialFormatter, self).get_field(field_name, args, kwargs)
            # Python 3, 'super().get_field(field_name, args, kwargs)' works
        except (KeyError, AttributeError):
            val=None,field_name 
        return val 

    def format_field(self, value, spec):
        # handle an invalid format
        if value==None: return self.missing
        try:
            return super(PartialFormatter, self).format_field(value, spec)
        except ValueError:
            if self.bad_fmt is not None: return self.bad_fmt   
            else: raise


def find_glossary_entries(filename):
    """
    Look through an org-mode file and pull out any glossary entries in it.
    """
    data = orgparse.load(filename)
    entries = []
    for heading in data.children:
        if "glossary" in heading.tags:
            for subheading in heading.children:
                entry_dict = dict(name = subheading.heading,
                                  description = subheading.body)
                if subheading.get_property("ABBR"):
                    entry_dict["abbreviation"] = subheading.get_property("ABBR")
                if subheading.get_property("ABBRPL"):
                    entry_dict["pl_abbreviation"] = subheading.get_property("ABBRPL")
                entries.append(entry_dict)
    return entries
        
def parse_org_file(filename):
    """
    Parse the contents of an org-mode format glossary file which
    stores a glossary using column-view.

    Parameters
    ----------
    filename : str
       The name of the file which contains the glossary.

    """
    base = PyOrgMode.OrgDataStructure()
    base.load_from_file(filename)
    entries = []
    for line in base.root.content:
        entry = {}
        if hasattr(line, "heading"):
        #     if not "glossary" in line.heading.lower():
        #         continue
            entry['name'] = line.heading
            entry['description'] = ""
            for descline in line.content:
                if hasattr(descline, "content"):
                    for orgproperty in descline.content:
                        if descline.TYPE == "DRAWER_ELEMENT":
                            try:
                                entry[orgproperty.name] = orgproperty.value#
                                #.replace("{","[").replace("}","]")
                                #print("+ {} : {}".format(orgproperty.name, orgproperty.value))
                            except AttributeError:
                                #print(orgproperty)
                                pass
                else:
                    entry['description'] += descline#.replace("\n", " ")
        entries.append(entry)
    return entries

def export_latex(entries):
    """
    Produce a LaTeX-formatted glossary, using `glossaries`.
    """
    fmt=PartialFormatter()
    gloss_entry = """
\\newglossaryentry{{{name}}}
{{
name={{{e[name]}}},
symbol={{{e[SYMBOL]}}},
descriptionplural={{{e[PLURAL]}}},
description={{{e[description]}}}
}}
"""
    
    for entry in entries:
        if "abbreviation" in entry:
           if "pl_abbreviation" in entry:
               pluralabb = "plural = {{{}}}".format(entry['pl_abbreviation'])
           else:
               pluralabb = ""
               
           print("\\newacronym[{}]{{{}}}{{{}}}{{{}}}".format(pluralabb, entry['abbreviation'].lower(), entry['abbreviation'], entry['name']))

    for entry in entries:
        if ("name" in entry) and ("description" in entry):
            output = fmt.format(gloss_entry, name=entry['name'].lower().replace(" ", "-"), e=entry)
            output.replace("\\n", " ")
            print(output)


def main():
    filename = sys.argv[1]
    entries = find_glossary_entries(filename) #parse_org_file(filename)
    export_latex(entries)

if __name__ == "__main__":
    main()
