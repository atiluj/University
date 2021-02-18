class Fixnum #pracownia 8 zadanie 1
    def czynniki
        listaCzynnikow = []
        pierwiastek = Math.sqrt(self).to_i
        i = 1
        while i <= pierwiastek
            if self % i == 0
                if i == self/i 
                    listaCzynnikow.push(i)
                else
                    listaCzynnikow.push(i)
                    listaCzynnikow.push(self/i)
                end
            end
            i = i + 1
        end
        return listaCzynnikow.sort 
    end

    def ack(m)
        n = self
        if n == 0
            return m + 1
        elsif m == 0
            return (n-1).ack(1)
        else 
            return (n-1).ack(n.ack(m-1))
        end
    end

    def doskonala
        n = self
        rozmiar = self.czynniki.length
        bezOstatniej = rozmiar - 1
        a = self.czynniki[0...bezOstatniej]
        if a.sum == n 
            return true
        else
            return false
        end
    end

    def slownie
        wynik = ""
        slownik = Hash["1" => "jeden ", "2"=> "dwa ", "3" => "trzy ", "4" => "cztery ", "5" => "pięć ", 
        "6" => "sześć ", "7" => "siedem ", "8" => "osiem ", "9" => "dziewięć ", "0" => "zero "]

        self.to_s.split('').each do |char|
            wynik += slownik[char]
        end 
        return wynik
    end
end


puts "Czynniki liczby 16"
puts 16.czynniki 
puts "Czy 6 jest doskonala?"
puts 6.doskonala
puts "Wynik wywołania 2.ack(1)"
puts 2.ack(1)
puts "1526 słownie:"
puts 1526.slownie 
