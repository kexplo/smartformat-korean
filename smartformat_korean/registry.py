# -*- coding: utf-8 -*-
"""
   smartformat.ext.korean.registry
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The Korean particle registry.

   :copyright: (c) 2016 by What! Studio
   :license: BSD, see LICENSE for more details.

"""
import re

from .particles import Euro, Ida, Particle


__all__ = ['Registry', 'registry']


def index_particles(particles):
    patterns, indices = [], {}
    for x, p in enumerate(particles):
        group = u'_%d' % x
        indices[group] = x
        patterns.append(u'(?P<%s>%s)' % (group, p.regex_pattern()))
    pattern = re.compile(u'|'.join(patterns))
    return pattern, indices


class Registry(object):

    __slots__ = ('particles', 'default', 'pattern', 'indices')

    def __init__(self, particles, default):
        self.particles = particles
        self.default = default
        self.pattern, self.indices = index_particles(particles)

    def _get_by_match(self, match):
        x = self.indices[match.lastgroup]
        return self.particles[x]

    def get(self, form):
        return self._get_by_match(self.pattern.match(form))

    def find(self, form):
        m = self.pattern.match(form)
        if m is None:
            return self.default
        return self._get_by_match(m)


#: The default registry for well-known Korean particles.
registry = Registry([
    # Simple allomorphic rule:
    Particle(u'이', u'가', final=True),
    Particle(u'을', u'를', final=True),
    Particle(u'은', u'는'),  # "은(는)" includes "은(는)커녕".
    Particle(u'과', u'와'),
    # Vocative particles:
    Particle(u'아', u'야', final=True),
    Particle(u'이여', u'여', final=True),
    Particle(u'이시여', u'시여', final=True),
    # Invariant particles:
    Particle(u'의', final=True),
    Particle(u'도', final=True),
    Particle(u'만'),
    Particle(u'에'),
    Particle(u'께'),
    Particle(u'뿐'),
    Particle(u'하'),
    Particle(u'보다'),
    Particle(u'밖에'),
    Particle(u'같이'),
    Particle(u'부터'),
    Particle(u'까지'),
    Particle(u'마저'),
    Particle(u'조차'),
    Particle(u'마냥'),
    Particle(u'처럼'),
    Particle(u'커녕'),
    # Special particles:
    Euro,
], default=Ida)
