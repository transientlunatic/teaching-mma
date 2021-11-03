from docutils import nodes

from sphinx.util.docutils import SphinxDirective


known_units = {"meter": "m",
         "second": "s",
         "parsec": "pc",
         "solmass": "\mathrm{M}_{\odot}"
}
need_tex = ["solmass"]



def setup(app):
    app.add_role('si', units('%s'))
    app.add_role('uncert', uncertainty('%s'))
    app.add_directive('simacros', MacroFactory)


    
class MacroFactory(SphinxDirective):
    """A custom directive that describes a glossary entry."""

    has_content = True
    required_arguments = 0

    option_spec = {
    }

    def run(self):
        signode = []
        for name, symbol in known_units.items():
            if name in need_tex:
                signode.append(nodes.math(text=f"\def\{name}{{{symbol}}}"))
            else:
                sym = f"\mathrm{{{symbol}}}"
                signode.append(nodes.math(text=f"\def\{name}{sym}"))
        return signode

    
def units(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        url = pattern % (text,)
        print(text.split(" "))

        lookups = known_units

        prefixes = {"centi": "c", "kilo": "k", "mega": "M"}
        newline = []
        for element in text.split(" "):
            element = element.split("^")
            print(element)

            # find prefixes
            for prefix, abbr in prefixes.items():
                if prefix in element[0]:
                    newline.append(nodes.abbreviation(text=nodes.Text(abbr), explanation=prefix))
                    element[0] = element[0].replace(prefix, "")
                    
            if element[0] in lookups:
                if element[0] in need_tex:
                    newline.append(nodes.math(text=lookups[element[0]]))
                else:
                    newline.append(
                        nodes.abbreviation(text=nodes.Text(lookups[element[0]]), explanation=element[0])
                    )
                newline.append(nodes.Text(" "))
                if len(element)==2:
                    newline.append((nodes.superscript(text=element[1])))
                    newline.append(nodes.Text(" "))
            else:
                newline.append(nodes.Text(element[0]+" "))
                
        node = nodes.inline()
        node += newline
        #nodes.reference(rawtext, text, refuri=url, **options)
        return [node], []
    return role

def uncertainty(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        newline = []
        number = text.split("+")[0]
        plus = text.split("+")[1].split("-")[0]
        minus = text.split("+")[1].split("-")[1]

        newline = [
            nodes.Text(number),
            nodes.superscript(text="+"+plus),
            nodes.subscript(text="-"+minus)
        ]
        node = nodes.inline()
        node += newline
        return [node], []
    return role
