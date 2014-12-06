pr.entity("seis_prov:as_A34J4DIDJ3", other_attributes=(
    ("prov:label", "Adjoint Source"),
    ("prov:type", "seis_prov:adjoint_source"),
    ("seis_prov:station_id", "BW.FURT.00.BHZ"),
    ("seis_prov:number_of_samples",
     prov.model.Literal(6000, prov.constants.XSD_INT)),
    ("seis_prov:sampling_rate",
     prov.model.Literal(10.0, prov.constants.XSD_DOUBLE)),
    ("seis_prov:units", "m/s"),
    ("seis_prov:adjoint_source_type", "Time Frequency Phase"),
    ("seis_prov:adjoint_source_type_uri", prov.model.Literal(
        "http://dx.doi.org/10.1111/j.1365-246X.2009.04368.x",
        prov.constants.XSD_ANYURI)),
    ("seis_prov:misfit_value", 1E-4))
)
