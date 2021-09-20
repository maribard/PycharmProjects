from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')


'''resize_mask = mask.resize((1015, 559))
resize_mask.putalpha(200)
resize_mask.show()
word_matrix.paste(resize_mask,(0,0),resize_mask)
word_matrix.show()'''




print(word_matrix.size)
print(mask.size)


resize_mask = mask.resize((1015, 559))
print(type(resize_mask))


word_matrix.paste(resize_mask, (0, 0), resize_mask)
word_matrix.show()
word_matrix.save('tttt.png')

#word_matrix_copy.save()
#word_matrix.show()
#resize_mask.show()
#word_matrix.show()
#mask.show()

