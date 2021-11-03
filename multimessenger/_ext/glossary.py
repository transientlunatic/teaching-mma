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
from sphinx.util.docutils import SphinxDirective

class GlossaryDirective(ObjectDescription):
    """A custom directive that describes a glossary entry."""

    has_content = True
    required_arguments = 1

    option_spec = {
        'label': directives.unchanged,
        'abbreviation': directives.unchanged,
        'abbreviationpl': directives.unchanged,
        'symbol': directives.unchanged,
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

class MacroFactory(SphinxDirective):
    """A custom directive that describes a glossary entry."""

    has_content = True
    required_arguments = 0

    option_spec = {
    }

    def run(self):
        glossary = self.env.get_domain('glossary')
        symbols = glossary.data['symbols']
        signode = []
        for name, symbol in symbols.items(): signode.append(nodes.math(text=f"\def\{name.split('.')[1].replace('-','')}{{{symbol}}}"))
        return signode


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
            dispname, typ, docname, anchor = entries[f"{abbreviation.lower()}"]
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
        'gls': XRefRole(),
        'symbol': XRefRole(),
        'mathsymbol': XRefRole()
    }
    directives = {
        'entry': GlossaryDirective,
        'macros': MacroFactory
    }
    indices = {
        AbbreviationIndex,
    }
    initial_data = {
        "entries": [],
        "entry": {},
        "symbols": {},
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
            match = [(docname, anchor, name, sig)
                     for name, sig, typ, docname, anchor, prio
                     in self.get_objects() if anchor.lower() == target.lower() ]


        elif typ=="gls":
            target = f"glossary:{target}".lower()
            match = [(docname, anchor, name, sig)
                     for name, sig, typ, docname, anchor, prio
                     in self.get_objects() if anchor.lower() == target.lower() ]

        elif typ=="symbol" or typ=="mathsymbol":
            target = f"glossary:{target}".lower()
            match = [(docname, anchor, name, sig)
                     for name, sig, typ, docname, anchor, prio
                     in self.get_objects() if anchor.lower() == target.lower() ]
            
        else:
            return None
        
        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]
            sig = match[0][3]
            if typ == "symbol":
                name = self.data['symbols'][match[0][2]]
                contnode = nodes.Text(name)
                return contnode
            elif typ == "mathsymbol":
                name = self.data['symbols'][match[0][2]]
                contnode = nodes.math(text=name)
                return contnode
            elif typ == "abbr":
                name = self.data['abbreviation-name'][match[0][2]]
                contnode = nodes.abbreviation(text=nodes.Text(name), explanation=sig)
            elif typ == "abpl" and (match[0][2] in self.data['abbreviation-plural']):
                name = self.data['abbreviation-plural'][match[0][2]]
                contnode = nodes.abbreviation(text=nodes.Text(name), explanation=sig)
            elif typ == "abpl":
                name = self.data['abbreviation-name'][match[0][2]]+"s"
                contnode = nodes.abbreviation(text=nodes.Text(name), explanation=sig)
            elif typ == "gls":
                name = self.data['entry'][match[0][2]]
                contnode = nodes.Text(name)
            else:
                name = match[0][2]
                contnode = nodes.Text(name)
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
        self.data['entry'][name] = signature
        if "abbreviation" in kwargs:
            self.data['abbreviation'][name] = signature
            self.data['abbreviation-name'][name] = kwargs['abbreviation']
        if "abbreviationpl" in kwargs:
            self.data['abbreviation-plural'][name] = kwargs['abbreviationpl']
        if "symbol" in kwargs:
            self.data['symbols'][name] = kwargs['symbol']


def setup(app):
    app.add_domain(GlossaryDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
