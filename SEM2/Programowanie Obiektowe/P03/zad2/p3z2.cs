using System;
//pracownia 3 zadanie 2
namespace p3z2
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> dic = new Dictionary<string, int>();
            Console.WriteLine("Stan słownika:");
            dic.Print();

            Console.WriteLine("Dodanie 3 słów: ");
            dic.Add("kot", 2);
            dic.Add("pies", 4);
            dic.Add("mucha", 7);         
            Console.WriteLine("Stan słownika:");
            dic.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Usunięcie słowa 'kot':");
            dic.Remove("kot");
            Console.WriteLine("Stan słownika:");
            dic.Print();
            Console.WriteLine("\n");

            Console.WriteLine("Wyszukanie słowa 'pies':");
            Console.WriteLine(dic.Find("pies"));
            Console.WriteLine("\n");

            Console.WriteLine("Wyszukanie słowa 'chomik':");
            Console.WriteLine(dic.Find("chomik"));
            Console.WriteLine("\n");
        }

        public class Lista<T>
        {
            class Element
            {
                public T value;
                public Element next;
                public Element prev;

                public Element(T val)
                {
                    this.next = null;
                    this.value = val;
                    this.prev = null;
                }
            }
            Element first;
            Element last;
            int length;

            public Lista()
            {
                this.first = null;
                this.last = null;
                length = 0;
            }

            public void Append(T x) //skopiowana z zadania 1
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

            public int Len()
            {
                return length;
            }

            public T get(int id)
            {
                if(id < 0 || id >= length) //>=?
                {
                    Console.WriteLine("Indeks muszi nie może byc mniejszy od 0 ani większy od rozmiaru listy.");
                    throw new System.IndexOutOfRangeException();
                }
                else
                {
                    int counter = 0;
                    Element temp = first;

                    while(temp != null)
                    {
                        if(counter == id)
                        {
                            return temp.value;
                        }
                        counter++;
                        temp = temp.next;
                    }
                    return temp.value;
                }
            }
            public void RemoveIndex(int idx)
            {
                if (idx < 0 || idx >= length)
                {
                    Console.WriteLine("Indeks muszi nie może byc mniejszy od 0 ani większy od rozmiaru listy.");
                    throw new System.IndexOutOfRangeException();
                }
                else if(idx == 0)
                {
                    if (length == 1)
                    {
                        first = null;
                        last = first;
                        length--;
                    }
                    else
                    {
                        first = first.next;
                        length--;
                    }
                }
                else
                {
                    Element v = first;
                    int iter = 0;
                    while (v != null)
                    {
                        if (iter == idx)
                        {
                            Element previous = v.prev;
                            Element nexxt = v.next;
                            previous.next = nexxt;
                            nexxt.prev = previous;
                            length--;
                            break;
                        }
                        v = v.next;
                        iter++;
                    }
                }
            }
        }
         public class Dictionary<Key, Value> where Key : IComparable<Key>
        {
            Lista<Key> keys;
            Lista<Value> values;
            int length;

            public Dictionary() //tworzymy slownik
            {
                keys = new Lista<Key>();
                values = new Lista<Value>();
                length = 0;
            }

            public void Add(Key k, Value v) //metoda dodaje 
            {
                keys.Append(k); 
                values.Append(v);
                length++;
            }

            public void Remove(Key k) //metoda odejmuje
            {
                int counter = 0;

                for(int i = 0; i < keys.Len(); i++)
                {
                    if (k.CompareTo(keys.get(i)) == 0)
                    {
                        keys.RemoveIndex(counter); 
                        values.RemoveIndex(counter);
                        length--;
                        break;
                    }
                    counter++;
                }
            }

            public Value Find(Key k) //metoda która znajduje
            {
                for(int i = 0; i < keys.Len(); i++)
                {
                    if (k.CompareTo(keys.get(i)) == 0)
                    {
                        return values.get(i);
                    }
                }
                Console.WriteLine("Nie ma w słowniku.");
                throw new System.Exception();
            }

            public void Print()
            {
                Console.Write("{");
                for (int i = 0; i < keys.Len(); i++)
                {
                    Console.Write("[" + keys.get(i) + ": " + values.get(i) + "], ");
                }
                Console.Write("}");
            }
        }
    }
}
