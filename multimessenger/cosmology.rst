Cosmology from multimessenger astronomy
=======================================

The observation of an abbr:em counterpart to GW170817 allowed the galaxy
it originated in to be identified. In turn this allowed the recession
velocity of the abbr:bns to be determined with high precision from its
redshift. The abbr:gw detection allows the distance to the source to be
measured directly (although with a fairly large uncertainty, thanks to a
degeneracy between the distance to the source and the angle at which it
is inclined relative to the observer.

Since the distance, :math:`d`, and recession velocity, :math:`v`, are
related by Hubble's Law,

.. raw:: latex

   \begin{equation}
   \label{eq:hubble-law}
   v = H_{0} d
   \end{equation}

if we know both :math:`v` and :math:`d` we can infer :math:`H_{0}`.

The distance to the source of GW170817 inferred from the abpl:gw is
:math:`d = \SI[parse-numbers=false]{48.8^{+2.9}_{-6.9}}{\mega\parsec}`,
and the measured recession velocity is
:math:`v = \SI{3017\pm166}{\kilo\meter\ \second^{-1}}`.

This allowed :math:`H_{0}` to be inferred to be
:math:`\SI[parse-numbers=false]{70.0^{+12.0}_{-8.0}}{\kilo\meter\ \second^{-1}\ \mega\parsec^{-1}}`
:raw-latex:`\cite{2017Natur.551...85A}`.

.. raw:: latex

   \begin{figure}
   \includegraphics[width=\textwidth]{figures/H0-inference}
   \caption{The posterior probability density function of the inferred value of the Hubble constant, $H_{0}$ using observations of GW170817, compared to the value inferred from Planck observations of the cosmic microwave background (green) and from supernovae (orange). The \gls{gw}-based inference is not sufficiently precise to resolve the tension between these two estimates.
   }
   \label{fig:h0-inference}
   \end{figure}

While we get the greatest amount of information from events which can be
localised by abbr:em observations, it is also possible to infer the
Hubble constant using only abbr:gw observations. This means that
abbr:bbh events can be used, which are much more frequently observed
than abbr:bns events.

In order to make inferences without knowing which galaxy the event
occurred in we need accurate three-dimensional galaxy catalogues. By
identifying a list of galaxies which lie within the localised volume
(through the sky localisation and distance estimate of the abbr:gw) we
can use a Bayesian analysis to combine the inferences from each
plausible galaxy to give an overall estimate
cite:2019arXiv190806050G,2019arXiv190806060T.

From the first two observation runs' detections it is possible to update
the GW170817-only estimate of :math:`H_{0}` to
:math:`\SI[parse-numbers=false]{68.0^{+14.0}_{-7.0}}{\kilo\meter\ \second^{-1}\  \mega\parsec^{-1}}`
:raw-latex:`\cite{2019arXiv190806060T}`.

.. raw:: latex

   \begin{figure}
   \includegraphics[width=\textwidth]{figures/H0-statistical}
   \caption{The posterior probability density function for $H_{0}$ inferred using a statistical method and observations from the O1 and O2 observing runs for advanced LIGO and Virgo. \cite{2019arXiv190806050G,2019arXiv190806060T}}
   \label{fig:det:advanced-timing}
   \end{figure}

GW follow-up of EM events
=========================

In addition to attempts to identify electromagnetic counterparts to
abbr:gw signals, there are ongoing efforts to identify abbr:gw signals
produced by events observed by abbr:em observatories. Thanks to the
near-continuous, all-sky, broadband observations made by a network of
abbr:gw detectors, it is possible to conduct searches for abbr:gw
counterparts in high-latency in recorded data (whereas an abbr:em
observatory may need to be pointed to the appropriate area of sky, for
example).

There have been targeted searches for abpl:gw from abpl:sn, motivated by
abbr:em observations. The sky localisation provided by the abbr:em
observation simplifies the process of searching for the abbr:gw signal
cite:2019arXiv190803584T.

Pulsars are the most promising source of continuous abpl:gw, and since
these are observed by radio telescopes, which can determine their
rotation frequency we can target searches for abpl:gw from pulsars both
by sky location and abbr:gw frequency (the abbr:gw frequency is twice
the rotation frequency, since abpl:gw are emitted from the quadrupole
mode). To date we've not been successful in detecting abpl:gw from
pulsars, but the non-detection allows us to place limits on the physical
properties of known pulsars cite:2019PhRvD..99l2002A. Pulsars are also
observed to *glitch* when observed in radio: a glitch is a sudden change
in the rotational frequency of the pulsar; the mechanism which causes
these is poorly understood, but may produce abpl:gw. The time at which
these glitches occur is well known from abbr:em observations, so
searches for these can be carried out over a short stretch of abbr:gw
data cite:2019PhRvD.100f4058K.

Observations are made of abpl:sgrb frequently, and abbr:bns events are
known to be a progenitor source for these events. These events are very
well localised in time, however gamma ray detectors are not normally
able to give a very precise sky localisation for an event, so a abbr:gw
search can be made over a short span of abbr:gw detector data, but a
large sky area cite:2019arXiv190701443T.
