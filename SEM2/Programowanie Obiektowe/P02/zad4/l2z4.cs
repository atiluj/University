using System;  //zadanie 4 lista 2

using System.Collections.Generic;

namespace ListaLeniwa
{
    class Program
    {
        static void Main(string[] args)
        {
            Lista_Leniwa lista = new Lista_Leniwa();   // 
            Console.WriteLine("Dlugosc listy na poczatku:  " + lista.size());  
            lista.element(100); //utworzenie 100 nowych elementów liczby 

            Console.WriteLine("Wartosc elementu nr 100: " + lista.element(100)); //wypisanie setnego elementu
            Console.WriteLine("Wartosc elementu nr 10:  " + lista.element(10));  //wypisanie dziesiątego elementu

            lista.element(10); //'utworzenie 10 elementów ' ma na celu pokazanie że nic to nie zmieni
            Console.WriteLine("Element nr 10:  " + lista.element(10)); //wartosc dziesiatego elementu sie nie zmieni, a długosc listy dalej jest równa 100
            Console.WriteLine("Dlugosc listy:  " + lista.size());

            lista.element(102); //wydłuzy liste o dwie nowe wartosci
            Console.WriteLine("Element nr 102: " + lista.element(102));
            Console.WriteLine("Dlugosc: " + lista.size());

            Lista_Primow lista2 = new Lista_Primow();

            //lista.element(10); 
            for (int i = 0; i <= 10; i++) //dopisanie to listy (kolejno) 10 liczb pierwszych 
            {
                Console.WriteLine(lista2.element(i));
            }
        }

        class Lista_Leniwa
        {
            public List<int> lista; //przechowuj
            protected int licznik; //przechowuje rozmiar

            public Lista_Leniwa()
            {
                lista = new List<int>();
                licznik = 0; // na początku ma rozmiar 0
            }

            public int size() //metoda która zwraca rozmiar
            {
                return licznik;
            }

            public virtual int element(int liczba)
            {
                int rozmiar = this.size(); //sprawdza jaki na razie lista ma rozmiar
                if (liczba <= rozmiar)
                {
                    return lista[liczba - 1];
                }
                else
                {
                    int g = liczba - rozmiar;
                    Random rand = new Random(); 

                    for (int i = 0; i < g; i++)
                    {
                        lista.Add(rand.Next());
                    }

                    licznik = liczba;
                }
                return lista[liczba - 1];
            }
        }

        class PrimeStream
        {
            private int licznik;

            public PrimeStream()
            {
                licznik = 1;
            }

            private bool czy_pierwsza(int licznik) //sprawdzenie czy licba jest pierwsza (dokladnie tej samej funkcji uzyłam w zadaniu 1 z tej listy)
            {
                double g = Math.Sqrt(licznik);

                for (int i = 2; i <= g; i++)
                {
                    if (licznik % i == 0)
                    {
                        return false;
                    }
                }

                return true;
            }

            public int next()
            {
                licznik++;

                while (czy_pierwsza(licznik) != true)
                {
                    licznik++;
                }

                return licznik;
            }
        }

        class Lista_Primow : Lista_Leniwa //klasa Lista_Primow dziedziczy po Lsita_Leniwa
        {
            protected PrimeStream pr;
            public Lista_Primow() //konstruktor
            {
                lista = new List<int>();
                licznik = 0;

                pr = new PrimeStream(); //kolejne liczby pierwsze
            }

            public override int element(int liczba)  //teraz wartosciami Lista_Primow beda kolejne liczby pierwsze
            {
                int rozmiar = this.size();

                if (liczba == 0)
                {
                    lista.Add(2); //pirwsza liczba pierwsza
                    pr.next();
                }

                if (liczba <= rozmiar)
                {
                    return lista[liczba];
                }
                else
                {
                    int g = liczba - rozmiar;

                    PrimeStream prime = new PrimeStream();

                    for (int i = 0; i < g; i++)
                    {
                        lista.Add(pr.next());
                    }
                }

                licznik = liczba;

                return lista[liczba];
            }
        }
    }
}
