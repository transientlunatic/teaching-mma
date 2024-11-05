The future: multi-band multimessenger astronomy
===============================================
.. glossary:macros::
.. simacros::

The current generation of :abbr:`GW` detectors are designed to operate in a
frequency range where the merger and ringdown components of a :abbr:`BNS`
or low-mass :abbr:`BBH` system will produce a detectable signal. However,
space-based detectors, such as :glossary:gls:`lisa`, will be able to make
observations at much lower frequencies. As a result the inspiral of
these events will be observable for a much longer period of time than is
currently possible.

For an inspiralling :abbr:`CBC` event the frequency of the inspiral signal
can be used to predict the time at which the two systems will merge
:cite:`1994PhRvD..50.7111S`. This means if the lowest frequency a detector
can measure an inspiral signal at is :math:`f_{\text{low}}` then the
time, :math:`t`, between observing the start of the inspiral and the
merger is approximately

.. math:: 

   \begin{align}
   \label{eq:sources:cbc:time-until-coalescence}
   t &\approx \frac{5}{256} \left( \frac{G \chirpmass}{c^3} \right)^{-\frac{5}{3}} ( \pi f_{\text{low}} )^{- \frac{8}{3}} \\
     &\approx 2.16 \left(\frac{\chirpmass}{1.22\,\mathrm{M}_{\odot}} \right)^{-\frac{5}{3}} \left( \frac{f_{\text{low}}}{{100}\,{\rm Hz}} \right)^{- \frac{8}{3}} \quad\text{sec}
   \end{align}

where :math:`\chirpmass` is the :glossary:gls:`chirp-mass`. For a :abbr:`BNS` system
the chirp mass will be around :math:`{1.25}\,{\mathrm{M}_{\odot}}`.

.. figure:: figures/inspiral-time.png
	    :name: fig:cbc:inspiral-time
	    :figwidth: 100%
	    :width: 100%

	    The physical time until coalescence for an inspiralling binary system, given a chirp mass (:math:`y`-axis), for the system, and a signal frequency (:math:`x`-axis).

..
   a) Advanced LIGO can detect signals at a frequency around as low as around :math:`\SI{25}{\hertz}`, however the third generation Einstein Telescope will be able to make observations down to around :math:`\SI{1}{\hertz}`.
      What is the increase in observation time achieved between the two detectors for a abbr:bns system? #

   b) Briefly discuss the advantages of adding more detectors to the detector network
   c) A CBC signal is observed by a detector network, and the chirp-mass is determined to be :math:`4.35\,\solMass` from the observed waveform.
      Assuming that the two objects have equal mass (that is, their mass-ratio is 1), and that the highest frequency of the signal is around :math:`\SI{20.8}{\kilo\hertz}`.
      What type of source is likely to have produced this signal?
      Why might we not expect to make an observation of this kind of event with the current network of detectors?

..
   a) The signal will be observable (although not necessarily detectable!)
   for around 87 seconds, but it will enter the ET band around 129 hours
   before coalescence, so ET has the potential to give several days' notice
   prior to the merger. In reality we probably only expect the advanced
   notice to be around an hour because of the length of time required to
   identify the signal in the data.

   b) Adding additional detectors both improves the sky localisation of the
   network (it substantially decreases the size of the plausible sky area
   which can contain any given source) and increases the live time of the
   network, by reducing the probability that no detectors are observing at
   any given time.

   c) The compactness ration is 1.44, which would imply a BBH, however the
   chirp-mass is very low, suggesting that the source may be a non-stellar
   (e.g. primordial) black hole. We're unlikely to see an event like this
   since the merger frequency is well above the frequency which advanced
   LIGO or Virgo is sensitive to.

   The amount of advance warning will depend on the strength of the
   abbr:bns signal, but all abbr:bns within :math:`\SI{40}{\mega\parsec}`
   should be localised an hour prior to the merger by third generation
   detectors cite:2018PhRvD..97l3014C.
