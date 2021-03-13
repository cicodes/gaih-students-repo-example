#Knowledge Competition

#On soru ve Cevabı tutan dictionary
questionAndAnswers = {
    "q1": {
        "question": "Bir ne?",
        "answer": "1000"
    },
    "q2": {
        "question": "İki ne?",
        "answer": "2000"
    },
    "q3": {
        "question": "Üç ne?",
        "answer": "3000"
    },
    "q4": {
        "question": "Bir ne?",
        "answer": "4000"
    },
    "q5": {
        "question": "İki ne?",
        "answer": "5000"
    },
    "q6": {
        "question": "Üç ne?",
        "answer": "6000"
    },
    "q7": {
        "question": "Bir ne?",
        "answer": "7000"
    },
    "q8": {
        "question": "İki ne?",
        "answer": "8000"
    },
    "q9": {
        "question": "Üç ne?",
        "answer": "9000"
    },
    "q10": {
        "question": "On ne?",
        "answer": "10000"
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
