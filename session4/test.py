# tuananh = ['Tuan Anh',22, 'Moc Chau', 2, True]
# tuananh = {
# }
#dictionary rỗng
# tuananh = {
#     "name": "Tuan Anh"
# }
#key phải là string
tuananh = {
"name": "Tuan Anh",
"age": 22,
"home": "Moc Chau",
"in_relationship": True,
"projecs": 4
}
# print(tuananh)
# print(tuananh['in_relationship'])
tuananh['extra_hours'] = 20
del tuananh['in_relationship']
print(tuananh)
