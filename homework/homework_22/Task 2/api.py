import requests
import json

class CatFacts:
    def __init__(self):
        self.url = 'https://meowfacts.herokuapp.com'

    def get_n_facts(self, amount=1, lang='eng-us'):
        response = requests.get(self.url, params={'count': amount, 'lang': lang})
        return response.json()


    def facts_to_file(self, dictionary):
        # Serializing json
        json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

        # Writing to sample.json
        with open("sample.json", "w", encoding="utf-8") as outfile:
            outfile.write(json_object)


if __name__ == '__main__':
    cat_facts = CatFacts()
    facts = cat_facts.get_n_facts(amount=5, lang='ukr')
    cat_facts.facts_to_file(facts)
    print(facts)