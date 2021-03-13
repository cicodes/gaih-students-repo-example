#Knowledge Competition

#On soru ve Cevabı tutan dictionary
questionAndAnswers = {
    "q1": {
        "question": "Ulu Önder Atatürk'ün doğum yılı nedir?",
        "answer": "1881"
    },
    "q2": {
        "question": "İstanbul'un kaç ilçesi vardır?",
        "answer": "39"
    },
    "q3": {
        "question": "Türkiye kaç coğrafi bölgeye ayrılmıştır?",
        "answer": "7"
    },
    "q4": {
        "question": "NBA'de kaç takım vardır?",
        "answer": "30"
    },
    "q5": {
        "question": "Bir Python kütüphanesi olan Pandas neyin kısaltmasıdır?",
        "answer": "Panel Data"
    },
    "q6": {
        "question": "Pandas kütüphanesinin temeli hangi yılda atılmıştır?",
        "answer": "2008"
    },
    "q7": {
        "question": "Numpy array'lerinin boyu sayısını yeniden düzenlemek için kullanılan metodun ismi nedir?",
        "answer": "reshape"
    },
    "q8": {
        "question": "Mantıksal doğru ve yanlış ifadelerini tanımlamak için kullanılan veri tipinin adı nedir?",
        "answer": "boolean"
    },
    "q9": {
        "question": "Programlamada fonksiyonları tanımlarken oluşturulan girdi değerlerine ne ad verilir(ingilizcesi)?",
        "answer": "Parameter"
    },
    "q10": {
        "question": "Programlamada fonksiyonları çağırırken gönderilen girdilere ne ad verilir(ingilizcesi)?",
        "answer": "argument"
    }
}

#Başlangıç Puanı
point = 0

print("GlobalAIHub Bilgi Yarışmasına Hoşgeldiniz. Yarışmamız 10 soruluktur. Başarılar :)")
#10 soru sorup aldığımız cevapları gerçek cevaplar ile karşılaştırıp doğru ise 10 puan yükseltiyoruz
for q in questionAndAnswers.values():
    userAnswer = input(q['question'])
    #userAnswer'ı ve answer'ı küçük harflere çeviriyoruz. 
    if(userAnswer.lower() == q['answer'].lower()):
        point += 10
    

#Tüm sorular cevaplandıktan sonra puanı kontrol edip Başarı durumunu söylüyoruz
if(point > 50):
    print("Tebrikler "+str(int(point/10)) + " soruya doğru cevap verdiniz. Yarışmayı başarıyla tamamladınız.")
else:
    print(str(int(point/5)) + " soruyu doğru cevapladınız. Diğer denemelerinizde başarılar dileriz." )
