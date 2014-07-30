pr.activity("seis_prov:rs_F87SF7SF78", other_attributes=(
    ("prov:label", "Resample"),
    ("prov:type", "seis_prov:interpolate"),
    ("seis_prov:frequency_domain_window", "Hanning"),
    ("seis_prov:new_starttime",
     prov.model.Literal(datetime(2013, 1, 2, 12, 10, 11),
                        prov.constants.XSD_DATETIME)),
    ("seis_prov:new_number_of_samples",
     prov.model.Literal(6000, prov.constants.XSD_INT)),
    ("seis_prov:new_sampling_rate",
     prov.model.Literal(100.0, prov.constants.XSD_DOUBLE))
))
