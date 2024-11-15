from django.contrib.gis.db.models import TextChoices


class Municipality(TextChoices):
    ADJUNTAS = "ADJUNTAS"
    AGUADA = "AGUADA"
    AGUADILLA = "AGUADILLA"
    AGUAS_BUENAS = "AGUAS_BUENAS"
    AIBONITO = "AIBONITO"
    ANASCO = "ANASCO"
    ARECIBO = "ARECIBO"
    ARROYO = "ARROYO"
    BARCELONETA = "BARCELONETA"
    BARRANQUITAS = "BARRANQUITAS"
    BAYAMON = "BAYAMON"
    CABO_ROJO = "CABO_ROJO"
    CAGUAS = "CAGUAS"
    CAMUY = "CAMUY"
    CANOVANAS = "CANOVANAS"
    CAROLINA = "CAROLINA"
    CATANO = "CATANO"
    CAYEY = "CAYEY"
    CEIBA = "CEIBA"
    CIALES = "CIALES"
    CIDRA = "CIDRA"
    COAMO = "COAMO"
    COMERIO = "COMERIO"
    COROZAL = "COROZAL"
    CULEBRA = "CULEBRA"
    DORADO = "DORADO"
    FAJARDO = "FAJARDO"
    FLORIDA = "FLORIDA"
    GUANICA = "GUANICA"
    GUAYAMA = "GUAYAMA"
    GUAYANILLA = "GUAYANILLA"
    GUAYNABO = "GUAYNABO"
    GURABO = "GURABO"
    HATILLO = "HATILLO"
    HORMIGUEROS = "HORMIGUEROS"
    HUMACAO = "HUMACAO"
    ISABELA = "ISABELA"
    JAYUYA = "JAYUYA"
    JUANA_DIAZ = "JUANA_DIAZ"
    JUNCOS = "JUNCOS"
    LAJAS = "LAJAS"
    LARES = "LARES"
    LAS_MARIAS = "LAS_MARIAS"
    LAS_PIEDRAS = "LAS_PIEDRAS"
    LOIZA = "LOIZA"
    LUQUILLO = "LUQUILLO"
    MANATI = "MANATI"
    MARICAO = "MARICAO"
    MAUNABO = "MAUNABO"
    MAYAGUEZ = "MAYAGUEZ"
    MOCA = "MOCA"
    MOROVIS = "MOROVIS"
    NAGUABO = "NAGUABO"
    NARANJITO = "NARANJITO"
    OROCOVIS = "OROCOVIS"
    PATILLAS = "PATILLAS"
    PENUELAS = "PENUELAS"
    PONCE = "PONCE"
    QUEBRADILLAS = "QUEBRADILLAS"
    RINCON = "RINCON"
    RIO_GRANDE = "RIO_GRANDE"
    SABANA_GRANDE = "SABANA_GRANDE"
    SALINAS = "SALINAS"
    SAN_GERMAN = "SAN_GERMAN"
    SAN_JUAN = "SAN_JUAN"
    SAN_LORENZO = "SAN_LORENZO"
    SAN_SEBASTIAN = "SAN_SEBASTIAN"
    SANTA_ISABEL = "SANTA_ISABEL"
    TOA_ALTA = "TOA_ALTA"
    TOA_BAJA = "TOA_BAJA"
    TRUJILLO_ALTO = "TRUJILLO_ALTO"
    UTUADO = "UTUADO"
    VEGA_ALTA = "VEGA_ALTA"
    VEGA_BAJA = "VEGA_BAJA"
    VIEQUES = "VIEQUES"
    VILLALBA = "VILLALBA"
    YABUCOA = "YABUCOA"
    YAUCO = "YAUCO"


class Classifications(TextChoices):
    AGUA = "AGUA"
    SREP_E = "SREP-E"
    SU = "SU"
    SRC = "SRC"
    SREP = "SREP"
    SREP_H = "SREP-H"
    SREP_EH = "SREP-EH"
    SREP_A = "SREP-A"
    VIAL = "VIAL"
    SREP_AE = "SREP-AE"
    SREP_AH = "SREP-AH"
    SREP_EA = "SREP-EA"
    SREP_EP = "SREP-EP"
    SURNP = "SURNP"
    SURP = "SURP"
    SREP_AP = "SREP-AP"
    SREP_P = "SREP-P"

class UseTypes(TextChoices):
    P = "P"
    V = "V"
    A = "A"
    D = "D"
    C = "C"
    p = "p"


RP_AOI = {
    "type": "FeatureCollection",
    "features": [
        {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": [
            [
                [
                -66.05644988749614,
                18.407599322858403
                ],
                [
                -66.05644988749614,
                18.395728461236544
                ],
                [
                -66.04310171909165,
                18.395728461236544
                ],
                [
                -66.04310171909165,
                18.407599322858403
                ],
                [
                -66.05644988749614,
                18.407599322858403
                ]
            ]
            ],
            "type": "Polygon"
        }
        }
    ]
}