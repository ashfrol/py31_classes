documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006"},
        {"type": "insurance", "number": "10006"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def update_shelf(shelf, document):
  if shelf in directories.keys():
    shelf_documents_list = directories[shelf] + [document]
    directories.update({shelf:shelf_documents_list})
  else:
    print(f'Создана новая полка с номером {shelf}')
    directories.update({shelf:[document]})

def get_person_by_document(documents):
  document_number = input('Введите номер документа: ')
  found = False
  for document in documents:
    if document['number'] == document_number:
      found = True
      name = document['name']
      print(f'Владелец документа: {name}')
  if found != True:
    print('Документ не найден')

def get_shelf_by_document(documents, shelves):
  document_number = input('Введите номер документа: ')
  found = False
  for directory, documents in directories.items():
    if document_number in documents:
      found = True
      print(f'Документ находится на {directory}-й полке')
  if found != True:
    print('Документ не найден')

def get_all_documents(documents):
  for document in documents:
    document_type = document['type']
    document_number = document['number']
    document_name = document['name']
    print(f'{document_type} "{document_number}" "{document_name}"')

def get_all_names(documents):
    names = []
    for document in documents:
        try:
            names.append(document['name'])
        except (Exception, KeyError) as e:
            print(f'Найден документ без поля {e}')
    names = set(names)
    print(f'Список имен владельцев документов {names}')

def add_new_document(documents, shelves):
  document_number = input('Введите номер нового документа: ')
  new_document_type = input('Введите тип нового документа: ')
  new_document_name = input('Введите имя и фамилию владельца нового документа: ')
  shelf_number = input('Введите номер полки для нового документа: ')
  documents.append({"type":new_document_type, "number":document_number, "name":new_document_name})
  update_shelf(shelf_number, document_number)
  print(f'Документ {new_document_type} с номером {document_number}, владелец {new_document_name}, добавлен на полку {shelf_number}')

def delete_document(documents, shelves):
  document_number = input('Введите номер документа, который нужно удалить: ')
  found = False
  for document in documents:
    if document['number'] == document_number:
      found = True
      documents.remove(document)
      for documents in directories.values():
        if document_number in documents:
          documents.remove(document_number)
      print(f'Документ с номером {document_number} успешно удален')
  if found != True:
    print('Документ не найден')

def move_document(shelves):
  document_number = input('Введите номер документа: ')
  found = False
  for documents in directories.values():
    if document_number in documents:
      found = True
      document_to_move = documents.pop(documents.index(document_number))
  if found != True:
    print('Документ не найден')
    return
  shelf_number = input('Введите номер полки, на которую нужно переставить документ: ')
  update_shelf(shelf_number, document_number)
  print(f'Документ с номером {document_number} переставлен на полку {shelf_number}')

def add_new_shelf(shelves):
  shelf_number = input('Введите номер новой полки: ')
  found = False
  if shelf_number in directories.keys():
    found = True
    print(f'Полка с номером {shelf_number} уже существует')
    return
  else:
    print(f'Создана новая полка с номером {shelf_number}')
    directories.update({shelf_number:[]})

def main():
  print('''Вы можете вызвать 4 команды:
    p - узнайте имя владельца по номеру документа;
    s – узнайте номер полки по номеру документа;
    l – получите список всех документов в формате: passport "2207 876234" "Василий Гупкин";
    n - получите список всех имен владельцев документов;
    a – добавьте новый документ на полку. Если полки с указанным номером не существует, будет создана новая;
    d – удалите документ по его номеру;
    m – переместите документ на новую полку. Если полки с указанным номером не существует, будет создана новая;
    as – добавьте новую полку;
    q - команда для завершения работы программы.''')
  while True:
    user_input = input('Введите команду: ')
    if user_input == 'p':
      get_person_by_document(documents)
    elif user_input == 's':
      get_shelf_by_document(documents, directories)
    elif user_input == 'l':
      get_all_documents(documents)
    elif user_input == 'n':
      get_all_names(documents)
    elif user_input == 'a':
      add_new_document(documents, directories)
    elif user_input == 'd':
      delete_document(documents, directories)
    elif user_input == 'm':
      move_document(directories)
    elif user_input == 'as':
      add_new_shelf(directories)
    elif user_input == 'q':
      break

main()
