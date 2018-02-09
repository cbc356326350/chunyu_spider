def get_hospital_id_from_url(url):
    def not_empty(s):
        return s and s.strip()
    return list(filter(not_empty, url.split('/')))[-1]


id = get_hospital_id_from_url("https://www.chunyuyisheng.com/pc/hospital/057d50b982d09d32/")
print(id)
