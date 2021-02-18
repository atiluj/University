using System;  //zadanie 1 lista 2

namespace Streams
{
    class Program
    {
        static void Main(string[] args)
        {
            IntStream integers = new IntStream();
            Console.WriteLine("IntStream:"); //kolejne liczby naturalne 

            for (int i = 0; i < 20; i++)
            {
                Console.Write(integers.next() + ", ");
                if (i == 3)
                {
                    integers.reset();
                }
            }

            PrimeStream prime = new PrimeStream(); //inicjalizacja i deklaracja
            Console.WriteLine("\n\nPrimeStream:");
            Console.Write(prime.next() + " ");
            Console.Write(prime.next() + " ");
            Console.Write(prime.next() + " ");
            Console.Write(prime.next() + " \n\n");

            RandomWordStream slowo = new RandomWordStream(); //inicjalizacja i deklaracja

            Console.WriteLine("Randomowe slowa");
            Console.WriteLine(slowo.next()); //dlugosci 2
            Console.WriteLine(slowo.next()); //dlugosci 3
            Console.WriteLine(slowo.next()); //dlugosci 5
            Console.WriteLine(slowo.next()); //dlugosci 7
        }

        class IntStream
        {
            protected int licznik; //zmienna licznik kolejne liczby naturalne protected znaczy że mogąjej używać tylko podklasy nie można jej użyc w main
            public IntStream() //konstruktor definiuje że zmienna licznik na start zawsze jest równa -1
            {
                licznik = -1; 
            }

            virtual public int next() //virutal oznacza że później w klasach dziedziczących możemy tą metode nadpisać
            {
                if (licznik == Int32.MaxValue)
                {
                    return -1;
                }
                else
                {
                    return ++licznik;
                }
            }

            virtual public bool eos() //eos end of stream sprawdza czy uż mmy koniec ciągu
            {
                if (Int32.MaxValue - 1 == licznik)
                    return true;
                else
                    return false;
            }

            virtual public void reset() //zaczyna od początku
            {
                licznik = -1; 
            }
        }

        class PrimeStream : IntStream //klasa PrimeStream, która dziedziczy po Intstream
        {
            private bool czy_pierwsza(int licznik) //funkcja prywatna która sprawdza czy liczba jest pierwsza
            {
                if (licznik < 2) return false;

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

            public override int next() //override to nadpisanie
            {
                if (licznik == Int32.MaxValue - 1)
                    return -1;

                licznik++;

                while (czy_pierwsza(licznik) == false && licznik < Int32.MaxValue)
                {
                    licznik++;
                }

                if (licznik == Int32.MaxValue)
                    return -1;
                else
                    return licznik;
            }
        }

        class RandomStream : IntStream //klasa RandomStream, która dziedziczy po Intstream
        {
            private Random rand; //dodatkowa zmienna
            public RandomStream() //konstruktor losuje radomowa liczbe
            {
                rand = new Random(Int32.MaxValue);
            }

            public override int next() //zwraca 0 - (Max - 1)
            {
                return rand.Next(0, Int32.MaxValue);
            }

            public override bool eos() //polecenie zadania eos zawsze fałszywe
            {
                return false;
            }
        }

        class RandomWordStream
        {
            private PrimeStream prime;
            private RandomStream rand;

            public RandomWordStream() //konstruktor
            {
                prime = new PrimeStream();
                rand = new RandomStream();
            }

            private char randchar() //0-25 zwraca jakąś literke
            {
                int ile = rand.next() % 26;
                return (char)('a' + ile);
            }

            public string next()
            {
                string result = "";
                int pierwsza = prime.next();

                for (int i = 0; i < pierwsza; i++)
                {
                    result += randchar();
                }
                return result;
            }
        }
    }
}
