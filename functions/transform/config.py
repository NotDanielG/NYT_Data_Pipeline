#NEED TO ACCOUNT FOR BEHAVIOR BETWEEN DICT OR ARRAY DATATYPE

from transform.calculation_utils import calculate_multi_authors

def get_nyt_full_overview_config():
    return {
        'key': 'api-key',
        'results': {
            'bestsellers_date': 'bestsellers_date',
            'lists': {
                'save_to_file': True,
                'list_id': 'list_id',
                'list_name': 'list_name',
                'list_name_encoded': 'list_name_official',
                'display_name': 'display_name',
                'books': {
                    'save_to_file': True,
                    'author': 'author',
                    'book_image': 'book_image_url',
                    'book_image_width': 'book_image_width',
                    'book_image_height': 'book_image_height',
                    'primary_isbn10': 'isbn10_id',
                    'primary_isbn13': 'isbn13_id',
                    'publisher': 'publisher',
                    'title': 'title',
                    'rank': 'rank',
                    'rank_last_week': 'rank',
                    'weeks_on_list': 'weeks_on_list'
                }
            }
        }
    }

def get_nyt_list_config():
    return {
        'key': 'api-key',
        'results': {
            'save_to_file': True,
            'bestsellers_date': 'bestsellers_date',
            'list_id': 'list_id',
            'list_name': 'list_name',
            'list_name_encoded': 'list_name_official',
            'display_name': 'display_name',
            'book_details': {
                'save_to_file': True,
                'title': 'title',
                'author': 'author',
                'publisher': 'publisher',
                'book_image': 'book_image_url',
                'book_image_width': 'book_image_width',
                'book_image_height': 'book_image_height',
                'primary_isbn10': 'isbn10_id',
                'primary_isbn13': 'isbn13_id',
            }
        },
    }

def get_google_columns():
    return {
        'key': 'key',
        'items': {
            'save_to_file': True,
            'description': 'description',
            'published_date': 'published_date',
            'calculated_values': [
                {
                    'func': calculate_multi_authors,
                    'args': ['authors']
                }
            ]
        }
    }

