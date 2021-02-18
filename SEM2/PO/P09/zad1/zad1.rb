class Funkcja #pracownia 9 zad 1
    def initialize(proc)
        if proc.instance_of?(Proc)
            @procedure = proc
        else
            raise 'error'
        end
    end

    def value(x)
        return @procedure.call(x)
    end

    def zerowe(a,b, eps)
        mid = (a+b)/2
        fa = value(a)
        fb = value(b)
        fmid = value(mid)
        if fa.abs < eps
            return fa
        elsif fb.abs < eps
            return fb
        elsif fmid.abs < eps
            return mid
        elsif fa*fmid < 0
            return zerowe(a, mid, eps)
        elsif fmid*fb < 0
            return zerowe(mid, b, eps)
        else
            return nil
        end
    end

    def pole(a, b)
        n = 100
        interval = (b-a).to_f/n
        result = 0
        result += value(a)/2
        result += value(b)/2
        for i in (1...n) do
            result += value(a + i * interval)
        end
        return interval*result
    end

    def poch(point)
        delta = 0.000000001
        return (value(point + delta) - value(point)) / delta
    end
end


f1 = Funkcja.new( proc {|x| x.abs})
print "Funkcja |x|:\n"
print "wartosc w 1: ", f1.value(1), "\n"
print "wartosc w -1: ", f1.value(-1), "\n"
print "wartosc w 0: ", f1.value(0), "\n"
print "Pochodna w punkcie 1: ", f1.poch(1), "\n"
print "Miejsce zerowe na przedziale [-5, 5] z eps 0.01: ", f1.zerowe(-5, 5, 0.01), "\n"
print "Pole pod wykresem na przedziale [0,20]: ", f1.pole(0,20), "\n"
f2 = Funkcja.new(proc {|x| (x**2)})
puts ""
print "Funkcja x^2:\n"
print "wartosc w 1: ", f1.value(1), "\n"
print "wartosc w -2: ", f2.value(-2), "\n"
print "wartosc w 2: ", f2.value(2), "\n"
print "Pochodna w punkcie 1: ", f2.poch(1), "\n"
print "Miejsce zerowe na przedziale [-5, 5] z eps 0.01: ", f2.zerowe(-5, 5, 0.01), "\n"
print "Pole pod wykresem na przedziale [0, 5]: ", f2.pole(0,5), "\n"
f3 = Funkcja.new(proc {|x| Math.sin(x)})
puts ""
print "Funkcja sin(x):\n"
print "wartosc w 1: ", f3.value(1), "\n"
print "wartosc w 0: ", f3.value(0), "\n"
print "wartosc w -1: ", f3.value(-1), "\n"
print "Pochodna w punkcie 1: ", f3.poch(1), "\n"
print "Miejsce zerowe na przedziale [0, 10] z eps 0.01: ", f3.zerowe(0, 10, 0.01), "\n"
print "Pole pod wykresem na przedziale [0,10]: ", f3.pole(0,10), "\n"
f3 = Funkcja.new(proc {|x| (x + 2)})
puts ""
print "Funkcja x+2:\n"
print "wartosc w 1: ", f3.value(1), "\n"
print "wartosc w 0: ", f3.value(0), "\n"
print "wartosc w -1: ", f3.value(-1), "\n"
print "Pochodna w punkcie 1: ", f3.poch(1), "\n"
print "Miejsce zerowe na przedziale [-5, 5] z eps 0.01: ", f3.zerowe(-5, 5, 0.01), "\n"
print "Pole pod wykresem na przedziale [0, 5]: ", f3.pole(0,5), "\n"
