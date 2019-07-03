# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime

class Sibisastrawi :
    def __init__(self):
        # create dictionary
        self.dictionary = set(line.strip() for line in open("root-words.txt"))
        # create stemmer
        factory = StemmerFactory()
        self.stemmer = factory.create_stemmer()

    def contains(self, s) :
        if (s in self.dictionary):
            return True
        else :
            return False

    def stem(self, s)  :
        stemResult = self.stemmer.stem(s)
        if (not self.contains(s))  :
            stemResult = self.generatePrefixBack(s, stemResult)
            stemResult = self.generateSuffixBack(s, stemResult)
        else  :
            stemResult = s
        
        return stemResult
    

    def removeUnecessaryCharacter(self, s)  :
        s = s.replace("\"", "").replace("[", "").replace("]", "")
        s = s.replace("“", "").replace("?", "").replace("", "")
        s.replace("'", "")
        s = s.replaceAll("[():|/,.not ]", "").lower()
        return s

    def printAuthor(self) :
        date = datetime.now()
        print("HASIL ALGORITMA STEMMING SIBISASTRAWI")
        print("Generated at " + str(date))
        print("@Author: M Nurilman Baehaqi")
        print("@Institution: Universitas Negeri Jakarta")

    def generatePrefixBack(self, s, stemResult)  :
        #first check if s is contain in dictionary
        if (not self.contains(s))  :
            
            prefixResult = ""
            if (len(s) > 2)  :
                twoFirstCharSequence = s[:2]
                #print("twoFirstCharSequence in prefix: " + twoFirstCharSequence)
                if (s.startswith("di")) :
                    prefixResult = prefixResult +"di "
                    prefixResult = prefixResult + self.generateDerivationPrefixBack(s.replace(twoFirstCharSequence, ""), prefixResult)
                elif (s.startswith("ke")) :
                    prefixResult = prefixResult +"ke "
                    prefixResult = prefixResult + self.generateDerivationPrefixBack(s.replace(twoFirstCharSequence, ""), prefixResult)
                elif (s.startswith("se"))  :
                    prefixResult = prefixResult +"se "
                    prefixResult = prefixResult + self.generateDerivationPrefixBack(s.replace(twoFirstCharSequence, ""), prefixResult)
                
                prefixResult = prefixResult + self.generateDerivationPrefixBack(s, prefixResult)
                
                stemResult = prefixResult + stemResult
                

        #print("result from generatePrefixBack: " + stemResult)
        return stemResult
    

    def generateDerivationPrefixBack(self, s, prefixResult)  :
        
        #Prevent output like = "me be beri kan" from input "memberikan"
        #should check if word before inflection and derivation suffix is exist in dictionary
        checkWordAfterDelSuffix = self.isWordExistInDictionaryAfterDeleteSuffix(s)
        if (not checkWordAfterDelSuffix)  :
            
            if (s.startswith("me"))  :
                prefixResult = prefixResult + "me "
                print(prefixResult)
            elif (s.startswith("te"))  :
                prefixResult = prefixResult + "te "
            elif (s.startswith("be"))  :
                prefixResult = prefixResult + "be "
            elif (s.startswith("pe"))  :
                prefixResult = prefixResult + "pe "
            
        return prefixResult
    

    def isWordExistInDictionaryAfterDeleteSuffix(self, s)  :
        len_ = len(s) - 1
        if (len_ <= 3)  :
            if (self.contains(s))  :
                return True
            else  :
                return False
            
        threeCharSequence = s[-3:]
        twoCharSequence = s[-2:]
        tempString = None

        if (s.endswith("lah"))  :
            tempString = self.removeDerivationSuffix(s.replace(threeCharSequence, ""))
        elif (s.endswith("kah"))  :
            tempString = self.removeDerivationSuffix(s.replace(threeCharSequence, ""))
        elif (s.endswith("ku"))  :
            tempString = self.removeDerivationSuffix(s.replace(twoCharSequence, ""))
        elif (s.endswith("mu"))  :

            tempString = self.removeDerivationSuffix(s.replace(twoCharSequence, ""))
        elif (s.endswith("nya"))  :
            tempString = self.removeDerivationSuffix(s.replace(threeCharSequence, ""))
        
        if (self.contains(tempString))  :
            return True
        else  :
            return False
    
    def removeDerivationSuffix(self, s)  :
        len_ = len(s) - 1
        if (len_ <= 3)  :
            return s
        
        threeCharSequence = s[-3:]
        twoCharSequence = s[-2:]
        oneCharSequence = s[-1:]

        if (s.endswith("i"))  :
            s = s.replace(oneCharSequence, "")
        elif (s.endswith("kan"))  :
            s = s.replace(threeCharSequence, "")
        elif (s.endswith("an"))  :
            s = s.replace(twoCharSequence, "")
        
        return s
    
    def generateSuffixBack(self, s, stemResult)  :

        #first check whether current word in current process is available in dictionary
        #Example input: ke be manfaat
        #Output: manfaat
        wordsOfStemmResult = stemResult.split(" ")
        lastPartOfStemmResult = wordsOfStemmResult[len(wordsOfStemmResult) - 1]
        if (self.contains(lastPartOfStemmResult) and not s.endswith(lastPartOfStemmResult))  :
            tempSuffix = ""
            tempInflectionResult = ""
            
            threeCharSequence = s[-3:]
            twoCharSequence = s[-2:]

            if (s.endswith("lah"))  :
                tempSuffix = tempSuffix + "lah"
                tempInflectionResult = self.generateInflectionSuffixBack(s.replace(threeCharSequence, ""))
                tempSuffix = tempSuffix  + tempInflectionResult
            elif (s.endswith("kah"))  :
                tempSuffix = tempSuffix +"kah"
                tempInflectionResult = self.generateInflectionSuffixBack(s.replace(threeCharSequence, ""))
                tempSuffix = tempSuffix  + tempInflectionResult
            elif (s.endswith("ku"))  :
                tempSuffix = tempSuffix +"aku"
                tempInflectionResult = self.generateInflectionSuffixBack(s.replace(twoCharSequence, ""))
                tempSuffix = tempSuffix  + tempInflectionResult
            elif (s.endswith("mu"))  :
                tempSuffix = tempSuffix +"kamu"
                tempInflectionResult = self.generateInflectionSuffixBack(s.replace(twoCharSequence, ""))
                tempSuffix = tempSuffix  + tempInflectionResult
            elif (s.endswith("nya"))  :
                tempSuffix = tempSuffix +"nya"
                tempInflectionResult = self.generateInflectionSuffixBack(s.replace(threeCharSequence, ""))
                tempSuffix = tempSuffix  + tempInflectionResult
            
            tempInflectionResult = self.generateInflectionSuffixBack(s)
            tempSuffix = tempSuffix  + tempInflectionResult
            #print("tempSuffix: " + tempSuffix.toString())
            stemResult = stemResult + " " + tempSuffix
        
        return stemResult
    

    def generateInflectionSuffixBack(self, s)  :
        if (s.endswith("i"))  :
            s = "i "
        elif (s.endswith("kan"))  :
            s = "kan "
        elif (s.endswith("an"))  :
            s = "an "
        else  :
            s = ""
        
        return s

if __name__ == "__main__":
    sibisastrawi = Sibisastrawi()
    sibisastrawi.printAuthor()
        
    word = "Mengambilkan Terpercaya tercerahkan persediaan berikan"
    word = word.lower()
    words = word.split()
    for w in words :
        stemmed = sibisastrawi.stem(w)
        print(stemmed)        
