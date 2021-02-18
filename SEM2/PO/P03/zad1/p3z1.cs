using System;
//pracownia 3 zadanie 1 
namespace p3z1
{
    class Program
    {
        static void Main(string[] args)
        {
            Lista<int> LISTA = new Lista<int>();
            Console.WriteLine("Stan listy na początku:");
            LISTA.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Dodajemy kolejno 1, 4, 7, 2 na koniec listy:");
            LISTA.AppendLast(1);
            LISTA.AppendLast(4);
            LISTA.AppendLast(7);
            LISTA.AppendLast(2);
            Console.WriteLine("Stan listy:");
            LISTA.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Dodajemy 0 na początek listy:");
            LISTA.AppendFirst(0);
            Console.WriteLine("Stan listy:");
            LISTA.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Sprawdzamy czy pusta:");
            LISTA.Empty();
            Console.WriteLine("\n");

            Console.WriteLine("Odejmujemy 3 ostatnie elementy:");
            LISTA.RemoveLast();
            LISTA.RemoveLast();
            LISTA.RemoveLast();
            Console.WriteLine("Stan listy:");
            LISTA.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Odejmujemy 2 pierwsze elementy:");
            LISTA.RemoveFirst();
            Console.WriteLine("Stan listy po usunieciu jedengo:");
            LISTA.Print();
            LISTA.RemoveFirst();
            Console.WriteLine("Stan listy po usunięciu drugiego:");
            LISTA.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Sprawdzamy czy pusta:");
            LISTA.Empty();
        }

        public class Lista<T>  //tworzymy klasę według polecenia
        {
            class Element //tworzymy osobną klasę, aby elemnty były elementami innej klasy (według polecenia) 
            {
                public T value; //pole zawieraące wartość typu T (według polecenia)
                public Element next; //odnośnik do elementu następnego
                public Element prev; //odnośnik do elemntu popredniego

                public Element(T val)
                {
                    this.next = null;
                    this.value = val;
                    this.prev = null;
                }
            }

            Element first;
            Element last;
            int length; //rozmiar listy /ilość elementów w liście

            //stwórzmy pustą liste
            public Lista()
            {
                this.first = null;
                this.last = null;
                length = 0;
            }

            public void Empty()
            {
                if (first == null)
                {
                    Console.WriteLine("Pusta lista");
                }
                else Console.WriteLine("Niepusta lista");
            }

            public void AppendFirst(T x)  //dodaje element na początek listy
            {
                Element NEW = new Element(x);

                if(first == null) //przypadek gdy mam pustą liste i may dodać jeden element
                {
                    first = NEW;
                }
                else
                {
                    NEW.next = first;
                    first.prev = NEW;//?
                    first = NEW;
                }

                length++; //zwiększamy rozmiar listy
            }

            public void AppendLast(T x) //dodaje element na koniec listy
            {
                Element NEW = new Element(x);

                if (first == null) //przypadek gdy mam pustą liste i may dodać jeden element
                {
                    first = NEW;
                    last = first;
                }
                else
                {
                    last.next = NEW;
                    NEW.prev = last;
                    last = NEW;
                }

                length++; //zwiększamy rozmiar listy
            }

            public T RemoveFirst() //usuwa element z początku listy
            {
                if(first == null)
                {
                    Console.WriteLine("Nie mozemy z pustej listy usunac elementu");
                    throw new System.IndexOutOfRangeException();
                }
                else
                {
                    T x = first.value; //przechowjemy wartośc ostatniego elemetu
                    first = first.next;

                    length--; //zmniejszamy rozmiar tablicy
                    return x; //zwrócenie usuniętej wartości
                }
            }

            public T RemoveLast() //usuwa element z końca listy
            {
                if (first == null)
                {
                    Console.WriteLine("Nie mozemy z pustej listy usunac elementu.");
                    throw new System.IndexOutOfRangeException();
                }
                else
                {
                    T x = last.value; //przechowjemy wartośc ostatniego elemetu
                    last = last.prev;
                    last.next = null;

                    length--; //zmienijszamy romiar listy
                    return x; //zwrócenie usuniętej wartośći
                }
            }

            // metoda pomocnicza do wypisywania listy na ekran
            public void Print()
            {
                if(first == null)
                {
                    Console.WriteLine("[]");
                }
                else
                {
                    Console.Write("[");
                    Element elem = first;

                    while (elem != null)
                    {
                        Console.Write(elem.value + ", ");
                        elem = elem.next;
                    }

                    Console.WriteLine("\b]");
                }
            }
        }
    }
}
