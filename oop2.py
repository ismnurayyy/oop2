
# Taskiniz sahmat ile bagli olaraq inheritance ve polymorphism istifade ederek bir numune yaratmaqdir
# class sahmat:
#     def __init__(self, figuradi, xanasayi, xanarengi, figursayi):
#         self.figuradi = figuradi
#         self.xanasayi = xanasayi
#         self.xanarengi = xanarengi
#         self.figursayi = figursayi

#     def __str__(self):
#         return "{}: {}, {}, {}".format(self.figuradi, self.xanasayi, self.xanarengi, self.figursayi)

#     def gedis(self):
#         print("{} gedisleri var".format(self.figuradi))
        

# qarafigurlar = sahmat("Qarafigurlar", 32, "ag-qara", 16)
# agfigurlar = sahmat("Agfigurlar", 32, "ag-qara", 16)

# print(vars(qarafigurlar))
# print(" bunlar {} dir ve {} figuru var".format(qarafigurlar.figuradi, qarafigurlar.figursayi))

#-----------------------------------------------------------------------------------------------------------------------------
# class figur():
#     def _init_(self):
#         print("figur yaradildi")
        
#     def menKimem(self):
#         print("Bu figurdur")
        
#     def gedis(self):
#         print("figurlarin ozunemaxsus gedisleri olur")
        
#     def vezife(self):
#         print("figurlarin zeif ve gucluleri olur")

# class vezir(figur):
#     def _init_(self):
#         super()._init_()
#         print("oyun yaradildi")
        
#     def menKimem(self):
#         print("Bu vezirdir")
        
#     def gedis(self):
#         print("vezir dioqonal, saquli ve ufuqi istiqametde hereket ede bilir")
        
#     def vezife(self):
#         print("vezir guclu figurdur")

# class piyada(figur):
#     def _init_(self):
#         super()._init_()
#         print("piyada yaradildi")
        
#     def menKimem(self):
#         print("Bu piyadadir")
        
#     def gedis(self):
#         print("piyada sadece saquli ve 1 dama hereket ede bilir")
        

# figur = figur()
# vezir = vezir()
# piyada = piyada()

# def test_gedis(test_sahmat):
#     test_sahmat.ucma()

# test_gedis(figur)
# test_gedis(piyada)
# test_gedis(vezir)
# #----------------------------------------------------------------------------------------------------
# class figur():
#     def _init_(self):
#         print("figur yaradildi")
        
#     def menKimem(self):
#         print("Bu figurdur")
        
#     def gedis(self):
#         print("figurlarin ozunemaxsus gedisleri olur")
        
#     def vezife(self):
#         print("figurlarin zeif ve gucluleri olur")

# class vezir(figur):
#     def _init_(self):
#         super()._init_()
#         print("oyun yaradildi")
        
#     def menKimem(self):
#         print("Bu vezirdir")
        
#     def gedis(self):
#         print("vezir dioqonal, saquli ve ufuqi istiqametde hereket ede bilir")
        
#     def vezife(self):
#         print("vezir guclu figurdur")

# vezir =vezir()
# vezir.menKimem()
# vezir.gedis()
# vezir.vezife()




