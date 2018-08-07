#!/usr/bin/env python3

class Geography:
    def __init__(self, name, places, places_kind):
        self.name = name
        self.places = places
        self.places_kind = places_kind

    def __contains__(self, key):
        return key in self.places

    def __len__(self):
        return len(self.places)

GEOGRAPHIES = [
        Geography(
            "United States",
            ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
             'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
             'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
             'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
             'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
             'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
             'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
             'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
             'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
             'Wyoming'],
            "state"),
        Geography(
            "Countries",
            ['USA', 'U.S.', 'Mexico', 'Haiti', 'Honduras', 'Virgin Islands', 'Grenada',
             'Puerto Rico', 'Brazil', 'Argentina', 'Zimbabwe', 'Guatemala',
             'Mozambique', 'Lesotho', 'South Africa', 'Botswana', 'Bolivia',
             'Peru', 'Swaziland', 'Chile', 'Colombia', 'Nicaragua', 'Ecuador',
             'Uruguay', 'Malawi', 'Panama', 'El Salvador', 'Costa Rica',
             'Belize', 'Canada', 'Venezuela', 'Jamaica', 'Paraguay',
             'Saint Vincent and the Grenadines', 'Saint Kitts and Nevis',
             'Saint Lucia', 'Cameroon', 'Kenya', 'Antigua and Barbuda',
             'New Zealand', 'United Kingdom', 'Trinidad and Tobago',
             'Dominica', 'Barbados', 'Montserrat'],
            "country"),
        Geography(
            "Mexico",
            ["Aguascalientes", "Baja California", "Baja California Sur",
             "Campeche", "Chiapas", "Mexico City", "Chihuahua", "Coahuila de Zaragoza",
             "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
             "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca",
             "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa",
             "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz de Ignacio de la Llave",
             "Ignacio de la Llave", "Yucatán", "Zacatecas", "Distrito Federal"],
            "state"),
        Geography(
            "Brazil",
            ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
             "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
             "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
             "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
             "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
             "Roraima", "Santa Catarina", "São Paulo", "Sergipe",
             "Tocantins"],
            "state"),
        Geography(
            "Peru",
            ["La Libertad", "Puno", "Lima"],
            "region"),
        Geography(
            "Chile",
            ["Región Metropolitana de Santiago"],
            "region"),
        Geography(
            "India",
            ["Andhra Pradesh"],
            "state"),
        Geography(
            "Swaziland",
            ["Hhohho", "Lubombo", "Manzini", "Shiselweni"],
            "region"),
        Geography(
            "Mozambique",
            ["Manica", "Sofala"],
            "province"),
        Geography(
            "South Africa",
            ["Gauteng", "Western Cape", "Kwazulu-Natal", "Free State",
             "Mpumalanga", "Eastern Cape", "Limpopo"],
            "province"),
        Geography(
            "France",
            ["Val-de-Marne"],
            "department"),
        Geography(
            "Costa Rica",
            ["Limón"],
            "province"),
        Geography(
            "China",
            ["Sichuan"],
            "province"),
        Geography(
            "New Zealand",
            ["Canterbury"],
            "region"),
        Geography(
            "United Kingdom",
            ["Buckinghamshire"],
            "county"),
        Geography(
            "Zimbabwe",
            ["Manicaland", "Harare", "Matabeleland South"],
            "province"),
        Geography(
            "El Salvador",
            ["Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán",
             "La Libertad", "La Paz", "La Unión", "Morazán",
             "San Miguel", "San Salvador", "San Vicente",
             "Santa Ana", "Sonsonate", "Usulután"],
            "department"),
        Geography(
            "Honduras",
            ["Atlántida", "Cortés"],
            "department"),
        Geography(
            "Haiti",
            ["Artibonite", "Centre", "Grand'Anse", "Nippes", "Nord",
             "Nord Est", "Nord Ouest", "Ouest", "Sud Est", "Sud"],
            "department"),
        Geography(
            "Canada",
            ["Ontario"],
            "province"),
        Geography(
            "Nigeria",
            ["Oyo"],
            "state"),
        Geography(
            "Bolivia",
            ["Oruro"],
            "department"),
        Geography(
            "Colombia",
            ["Cundinamarca", "Valle del Cauca"],
            "department"),
        Geography(
            "Malawi",
            ["Dowa"],
            "district"),
        Geography(
            "Argentina",
            ["Córdoba"],
            "province"),
        ]


CITIES = {
        "Cuneo": "Italy",
        "Bergamo": "Italy",
        "São Paulo": "Brazil",
        "Paris": "France",
        "Zürich (de)": "Switzerland",
        "Maseru": "Lesotho",
        "Adis Abeba": "Ethiopia",
        }
