from collections import defaultdict

from docutils.parsers.rst import directives
from docutils import nodes
from docutils.parsers.rst import Directive, Parser

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain
from sphinx.domains import Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode

class GlossaryDirective(ObjectDescription):
    """A custom directive that describes a glossary entry."""

    has_content = True
    required_arguments = 1

    option_spec = {
        'label': directives.unchanged,
        'abbreviation': directives.unchanged,
        'abbreviationpl': directives.unchanged,
    }

    def handle_signature(self, sig, signode):
        signode += nodes.Text(self.arguments[0])
        if "abbreviation" in self.options:
            signode += nodes.Text(f" ({self.options['abbreviation']})")
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append('glossary' + ':' + self.options['label'].lower())
        if 'noindex' not in self.options:
            
            glossary = self.env.get_domain('glossary')

            # options = dict(abbreviation=self.options['abbreviation'],
            #                abbreviationpl=self.options['abbreviationpl'])
            
            glossary.add_entry(self.arguments[0],
                               #label=self.options['label'],
                               **self.options)


class AbbreviationIndex(Index):
    """A custom index that creates an recipe matrix."""

    name = 'abbreviation'
    localname = 'Abbreviation Index'
    shortname = 'Abbreviations'

    def generate(self, docnames=None):
        content = defaultdict(list)

        entries = {name.lower(): (dispname, typ, docname, anchor)
                   for name, dispname, typ, docname, anchor, _
                   in self.domain.get_objects()}
        
        abbreviations = self.domain.data['abbreviation']
        abbreviations_r= defaultdict(list)

        for abbreviation, definition in abbreviations.items():
                abbreviations_r[definition] = abbreviation
                
        for definition, abbreviation in abbreviations_r.items():
            dispname, typ, docname, anchor = entries[f"glossary.{abbreviation.lower()}"]
            dispname = f"{abbreviation}: {definition}"
            content[abbreviation].append((dispname, 0, docname, anchor, "", '', ""))

        content = sorted(content.items())
        
        return content, True


class GlossaryDomain(Domain):

    name = 'glossary'
    label = 'Glossary'
    roles = {
        'abbr': XRefRole(),
        'abpl': XRefRole(),
    }
    directives = {
        'entry': GlossaryDirective,
    }
    indices = {
        AbbreviationIndex,
    }
    initial_data = {
        "entries": [],
        "abbreviation": {},
        "abbreviation-name": {},
        "abbreviation-plural": {}
    }
    
    def get_full_qualified_name(self, node):
        return '{}.{}'.format('recipe', node.arguments[0])

    def get_objects(self):
        for obj in self.data['entries']:
            yield(obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        if typ=="abbr" or typ=="abpl":
            target = f"glossary:{target}".lower()

            # for name, sig, typ, docname, anchor, prio in self.get_objects():
            #     print(name, typ, anchor.lower(), sig)
        
            match = [(docname, anchor, name, sig)
                     for name, sig, typ, docname, anchor, prio
                     in self.get_objects() if anchor.lower() == target.lower() ]


        else:
            return None
        
        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            if typ == "abbr":
                name = self.data['abbreviation-name'][match[0][2]]
            elif typ == "abpl" and (match[0][2] in self.data['abbreviation-plural']):
                name = self.data['abbreviation-plural'][match[0][2]]
            elif typ == "abpl":
                name = self.data['abbreviation-name'][match[0][2]]+"s"
            else:
                name = match[0][2]
            sig = match[0][3]
            contnode = nodes.abbreviation(text=nodes.Text(name), explanation=sig)
            #contnode.elements = [nodes.Text(name)]
            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            print('Awww, found nothing')
            return None

    def add_entry(self, signature, **kwargs):
        """Add a new entry to the glossary."""
        if "label" in kwargs:
            label = kwargs['label']
            name = f"glossary.{label}"
            anchor = f"glossary:{label}"
        else:
            name =  f"glossary.{signature}"
            anchor = f"glossary-{signature}"

        self.data['entries'].append(
            (name, signature, "Glossary", self.env.docname, anchor, 0)
        )

        if "abbreviation" in kwargs:
            self.data['abbreviation'][kwargs['abbreviation']] = signature
            self.data['abbreviation-name'][name] = kwargs['abbreviation']
        if "abbreviationpl" in kwargs:
            self.data['abbreviation-plural'][name] = kwargs['abbreviationpl']


def setup(app):
    app.add_domain(GlossaryDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
