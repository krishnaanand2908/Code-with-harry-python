print("KrishnaFord Dictionary")

choose = input("Choose your word:\n 1.cow\n 2.abandon\n 3.computer\n 4.hair\n 5.code\n")

language = input("Choose your language [E/H]")

if choose == "1":
    if language == "E":
        print("a large female animal that is kept on farms to produce milk")
    elif language == "H":
        print("दूध के लिए पाला जानेवाला मादा पशु; गाय")
    else:
        print("Restart the program and choose a language.")
        
elif choose == "2":
    if language == "E":
        print("to leave somebody/something that you are responsible for, usually permanently")
    elif language == "H":
        print("किसी प्राणी या वस्‍तु को, जिस का उत्तरदायित्‍व आप पर है, प्रायः सदा के लिए छोड़ देना")
    else:
        print("Restart the program and choose a language.")
        
elif choose == "3":
    if language == "E":
        print("an electronic machine that can store, find and arrange information, calculate amounts and control other machines")
    elif language == "H":
        print("जानकारी संचित करने, ढूँढ़ने व व्‍यवस्थित करने, परिकलन करने व अन्‍य मशीनों पर नियंत्रण रख पाने वाली एक इलेक्‍ट्रॉनिक मशीन; कंप्‍यूटर")
    else:
        print("Restart the program and choose a language.")
        
elif choose == "4":
    if language == "E":
        print("the mass of long thin strands that grow on the head and body of people and animals; one such strand")
    elif language == "H":
        print("बाल, केश")
    else:
        print("Restart the program and choose a language.")
        
elif choose == "5":
    if language == "E":
        print("a system of words, letters, numbers, etc. that are used instead of the real letters or words to make a message or information secret")
    elif language == "H":
        print("शब्‍दों, अक्षरों, संख्‍याओं आदि से बनी गुप्‍त संकेत-पद्घति; कूट-भाषा")
    else:
        print("Restart the program and choose a language.")

else:
    print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR\n ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR\n ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
    
print("Have a good day")
        