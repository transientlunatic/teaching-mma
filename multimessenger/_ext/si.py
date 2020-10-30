from docutils import nodes

def setup(app):
    app.add_role('si', autolink('%s'))

def autolink(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        url = pattern % (text,)
        print(text.split(" "))

        lookups = {"meter": "m",
                   "second": "s"
                   }
        prefixes = {"centi": "c", "kilo": "k"}
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
                newline.append(
                    nodes.abbreviation(text=nodes.Text(lookups[element[0]]), explanation=element[0]))
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
