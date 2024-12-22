import json
import os
from notion_client import Client

api = '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'
client = Client(auth=api) # token: インテグレーションのシークレット情報
print ('---set apikey!')
os.environ['NOTION_TOKEN'] = api


def read_notion_database(database_id):
    response = client.databases.query(
        **{
            "database_id": database_id,
        }
    )

    #print(response)
    return response

def getpath():
    #このスクリプトのあるディレクトリのパスを取得
    r = str(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
    #print (r)
    return r

def save_dict_to_json(data):
    """
    辞書を指定されたファイルパスのJSONファイルに保存します。

    Parameters:
    - data (dict): 保存するデータ。
    - filepath (str): JSONファイルのパス。

    Returns:
    None
    """
    filepath= getpath() + "/exp.json"

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def find_data(dictn = {}):

    if 'type' in dictn.keys():
        
        typen = dictn['type']

        getdata = dictn[typen]

        if typen == 'rich_text':
            #list
            if len(getdata) > 0:
                return getdata[0]['plain_text']
                
        elif typen == 'select':
            #dict?
            if type(getdata) == dict:
                return getdata['name']
        elif typen == 'relation':
            #dict?
            if len(getdata) > 0:
                return getdata[0]['id']
            
        elif typen == 'title':
            #list
            if len(getdata) > 0:
                return getdata[0]['plain_text']
            
        return None

    else:
        #print ('---no type key!')
        return None

def make_game_dict(database_id = '164bd4ce94e0806391d6faeda15e4227'):

    hide = ["ID","GoTo02_re","GoTo01_re"]

    r = read_notion_database(database_id)

    print ('---read notion database!')

    print(type(r))
    dict_orig_list = []

    if 'results' in r.keys():
        dict_orig_list = r['results']

    else:
        print ('---no results!')
        return None

    #辞書のリストを整形
    #idをkeyに

    result_dict = {}

    for dict_orig in dict_orig_list:
        
        if 'properties' in dict_orig.keys():

            nkey = dict_orig['id']

            dint_temp = {}

            for o in dict_orig['properties'].keys() :
                
                if o not in hide:
                    #continue
                    #notionのプロパティの中からplane_textや

                    dint_temp[o] = find_data(dict_orig['properties'][o])

            result_dict[nkey] = dint_temp

    print ('---make game dict!')
    return result_dict

def main():
    game_dict = make_game_dict()

    print (game_dict)
    print (len(game_dict))
    print (getpath() + "/exp.json")
    save_dict_to_json(game_dict)

main()