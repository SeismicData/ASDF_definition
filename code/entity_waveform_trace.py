pr.entity("seis_prov:wf_A34J4DIDJ3", other_attributes=(
    ("prov:label", "Waveform Trace"),
    ("prov:type", "seis_prov:waveform_trace"),
    ("seis_prov:station_id", "BW.FURT.00.BHZ"),
    ("seis_prov:starttime",
     prov.model.Literal(datetime(2013, 1, 2, 12, 10, 11),
                        prov.constants.XSD_DATETIME)),
    ("seis_prov:number_of_samples",
     prov.model.Literal(6000, prov.constants.XSD_INT)),
    ("seis_prov:sampling_rate",
     prov.model.Literal(100.0, prov.constants.XSD_DOUBLE)),
    ("seis_prov:units", "m/s")
    )
)
