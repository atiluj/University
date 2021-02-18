using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//lista 4 zadanie 2

namespace l4z2_PrimeCollection
{

    public class Primes : IEnumerator 
    {
        private int counter;

        public Primes() //konstruktor
        {
            counter = 1;
        }

        public bool MoveNext()
        {
            counter++; 
            for (int i = 2; i < counter; i++)
            {
                if (counter % i == 0)
                {
                    counter++;
                    i = 2;
                }
                else
                {
                    continue;
                }
            }
            return counter < int.MaxValue; //int_MAX =2147483647             
        }
     
        public void Reset()
        {
            counter = 1;
        }

        public object Current
        {
            get
            {
                return counter;
            }
        }
    }

    class PrimeCollection : IEnumerable //według polecenia PrimeCollection implementującą interfejs IEnumerable
    {
        public IEnumerator GetEnumerator() //Zwraca moduł wyliczający, który iteruje po kolekcji.
        {
            return new Primes();
        }

        public static void Main() 
        {
            PrimeCollection pc = new PrimeCollection();
            foreach (int p in pc)  //foreach słuzy do iteracji w kolekjci. Wykonuje instrukcję lub blok instrukcji dla każdego elementu wystąpienia.
                Console.WriteLine(p);
        }
    }
}
