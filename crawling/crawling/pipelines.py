from itemadapter import ItemAdapter
from restmember.models import Member
import jsonschema

from rest_framework.exceptions import ParseError

class CrawlingPipeline:
    
    def process_item(self, item, spider):
        name = item['name'] 
        birth_date = item['birth_date'] 
        birth_place = item['birth_place']
        profession = item['profession']
        languages = item['languages'] 
        political_force = item['political_force'] 
        email = item['email'] 

        Member.objects.create(
            name = name,
            birth_date = birth_date,
            birth_place = birth_place,
            profession = profession,
            languages = languages,
            political_force = political_force,
            email = email,
        )
 
        return item