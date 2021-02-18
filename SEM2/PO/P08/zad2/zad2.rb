#pracownia 8 zadanie 2
klucz = { "a" => "b", "b" => "r","r" => "y", "y" => "u", "u" => "a",
    "c" => "d", "d" => "e", "e" => "f", "f" => "g", "g" => "h", "h" => "i", "i" => "j", "j" => "k", 
    "k" => "l", "l" => "m", "m" => "n", "n" => "o", "o" => "p", "p" => "c", "s" => "t", "t" => "w", "w" => "s"}

class Jawna
    def initialize(msg)
        @message = msg
    end 

    def zaszyfruj(klucz)
        wynik = ""        
        @message.split("").each do |sign|
            wynik += klucz[sign]
            #puts wynik
        end 

        wyn = Zaszyfrowana.new(wynik)
        return wyn 
    end 

    def to_s #z polecenia
        @message
    end
end 
        
        
class Zaszyfrowana
    def initialize(szyfr)
        @szyfr = szyfr 
    end 

    def to_s
        @szyfr 
    end

    def odszyfruj(klucz)
        odwrKlucz = klucz.invert
        wyn = ""
        @szyfr.split("").each do |char|
            wyn += odwrKlucz[char]
        end
        wynik = Jawna.new(wyn)
        return wynik 
    end
end

test = Jawna.new("ruby")
print "Wersja oryginalna: "
puts test.to_s
szyfrTest = test.zaszyfruj(klucz)
print "Zaszyfrowane: " 
puts szyfrTest.to_s
backToOrig = szyfrTest.odszyfruj(klucz).to_s 
print "Odszyfrowane: "
puts backToOrig
