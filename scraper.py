import requests
from bs4 import BeautifulSoup
import csv

file = []

country_list = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'The Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'China', 'Colombia', 'Democratic Republic of the Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Denmark', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Finland', 'France', 'Gabon', 'The Gambia', 'Georgia (country)', 'Germany', 'Ghana', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Republic of Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Lithuania', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Federated States of Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Kingdom of the Netherlands', 'New Zealand', 'Nicaragua', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'São Tomé and Príncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe']
def main():
    for loop in country_list:
        page = requests.get(f"https://en.wikipedia.org/wiki/{loop}")
        src = page.content
        soup = BeautifulSoup(src,"html.parser")
        country_name = soup.find("span",class_="mw-page-title-main")
        if country_name:
            country_name = country_name.text.strip()
        country_flag = soup.find("a",class_="mw-file-description")
        if country_flag:
            country_flag ="https://en.wikipedia.org" + country_flag.get("href")
        country_capital = soup.find("td",class_="infobox-data").a
        if country_capital:
            country_capital = country_capital.text

        file.append({"Country Name":country_name,
                    "Country Capital":country_capital,
                    "Country Flag":country_flag,
                    })
        
        keys = file[0].keys()

    with open("Countries.csv","w",newline="",encoding="UTF-8") as f:
        writer = csv.DictWriter(f,keys)
        writer.writeheader()
        writer.writerows(file)
        print("File Created")

main()