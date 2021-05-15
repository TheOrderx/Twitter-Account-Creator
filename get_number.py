import smsactivateru as seller
from smsactivateru import SmsTypes, SmsService
import utils

wrapper = seller.Sms(utils.get_sms_activate_ru_api())

def get_number(country):
    activation = seller.GetNumber(service=SmsService().Twitter,
                                  country=country).request(wrapper)
    data = [str(activation.id), str(activation.phone_number), str(activation.phone_number)[:len(str(activation.phone_number)) - 10], parse_code(country)]
    data.append(str(data[1][len(data[2]):]))
    data.append(activation)
    return data


def parse_code(code):
    return {'0': "RU",
            '1': "UA",
            '2': "KZ",
            '3': "CN",
            '4': "PH",
            '5': "MM",
            '6': "ID",
            '7': "MY",
            '10': "VN",
            '11': "KG",
            '12': "US",
            '13': "IL",
            '14': "HK",
            '15': "PL",
            '16': "UK",
            '17': "MG",
            '18': "CG",
            '19': "NG",
            '20': "MO",
            '21': "EG",
            '23': "IE",
            '24': "KH",
            '25': "LA",
            '26': "HT",
            '27': "CI",
            '28': "GM",
            '29': "RS",
            '30': "YE",
            '31': "ZA",
            '32': "RO",
            '34': "EE",
            '35': "AZ",
            '36': "CA",
            '37': "MA",
            '38': "GH",
            '39': "AR",
            '40': "UZ",
            '41': "CM",
            '42': "TG",
            '43': "DE",
            '44': "LT",
            '45': "HR",
            '47': "IQ",
            '48': "NL"
            }.get(code)