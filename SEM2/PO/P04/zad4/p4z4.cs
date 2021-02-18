using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//pracownia 4 zadanie 4
namespace zadanie4_gramatyki
{
    class S
    {
        public String napis;
        public S()
        {
            napis = "";
        }

        public static String[] mozliwosci = { "AA", "BB", "AB" };
        public static char[] drzewo = new char[2];

        public virtual char[] Losuj()
        {
            Random rand = new Random();
            String ciag = mozliwosci[rand.Next(3)];
            drzewo[0] = ciag[0];
            drzewo[1] = ciag[1];
            return drzewo; 
        }
        public virtual String buduj_drzewo(char[] drzewo)
        {
            if (drzewo[0] == 'A')
            {
                A d_A = new A();
                char[] d1 = d_A.Losuj();
                napis += d_A.buduj(d1);
                Console.Write("Aktualny napis:");
                Console.WriteLine(napis);
                if (drzewo[1] == 'A')
                {
                    A d_A2 = new A();
                    char[] d2 = d_A2.Losuj();
                    napis += d_A2.buduj(d2);
                    Console.Write("Aktualny napis:");
                    Console.WriteLine(napis);
                }
                else if (drzewo[1] == 'B')
                {
                    B d_B = new B();
                    char[] d2 = d_B.Losuj();
                    napis += d_B.buduj(d2);
                }
            }
            else if (drzewo[0] == 'B')
            {
                B d_B = new B();
                char[] d1 = d_B.Losuj();
                napis += d_B.buduj(d1);
                Console.Write("Aktualny napis:");
                Console.WriteLine(napis);
                if (drzewo[1] == 'A')
                {
                    A d_A = new A();
                    char[] d2 = d_A.Losuj();
                    napis += d_A.buduj(d2);
                    Console.Write("Aktualny napis:");
                    Console.WriteLine(napis);
                }
                else if (drzewo[1] == 'B')
                {
                    B d_B2 = new B();
                    char[] d2 = d_B2.Losuj();
                    napis += d_B2.buduj(d2);
                    Console.Write("Aktualny napis:");
                    Console.WriteLine(napis);
                }
            }

            Console.Write("Koncowe slowo: ");
            return napis;
        }
    }

    class A
    {
        public String napis;
        public static String[] mozliwosci = { "Aa", "AA", "ac" };
        public static char[] drzewo = new char[2];

        public virtual char[] Losuj()
        {
            Random rand = new Random();
            String ciag = mozliwosci[rand.Next(3)];
            Console.WriteLine(ciag);
            drzewo[0] = ciag[0];
            drzewo[1] = ciag[1];
            return drzewo;
        }

        public virtual String buduj(char[] drzewo)
        {
            if (drzewo[0] == 'a' || drzewo[0] == 'c')
            {
                napis = napis + drzewo[0];
                if (drzewo[1] == 'a' || drzewo[1] == 'c')
                {
                    napis = napis + drzewo[1];
                }
                else if (drzewo[1] == 'A')
                {
                    return this.buduj(Losuj());
                }
            }
            else if (drzewo[0] == 'A')
            {
                if (drzewo[1] == 'a' || drzewo[1] == 'c')
                {
                    napis = napis + drzewo[1];
                }
                else if (drzewo[1] == 'A')
                {
                    return this.buduj(Losuj());
                }
                return this.buduj(Losuj());
            }

            return napis;
        }
    }

    class B
    {
        public String napis;
        public static String[] mozliwosci = { "Bb", "BB", "bd" };
        public static char[] drzewo = new char[2];


        public virtual char[] Losuj()
        {
            Random rand = new Random();
            String ciag = mozliwosci[rand.Next(3)];
            Console.WriteLine(ciag);
            drzewo[0] = ciag[0];
            drzewo[1] = ciag[1];
            return drzewo;
        }

        public virtual String buduj(char[] drzewo)
        {
            if (drzewo[0] == 'b' || drzewo[0] == 'd')
            {
                napis = napis + drzewo[0];
                if (drzewo[1] == 'b' || drzewo[1] == 'd')
                {
                    napis = napis + drzewo[1];
                    //return (napis);
                }
                else if (drzewo[1] == 'B')
                {
                    return this.buduj(Losuj());
                }
            }
            else if (drzewo[0] == 'B')
            {
                if (drzewo[1] == 'b' || drzewo[1] == 'd')
                {
                    napis = napis + drzewo[1];
                }
                else if (drzewo[1] == 'B')
                {
                    return this.buduj(Losuj());
                }
                return this.buduj(Losuj());

            }

            return napis;
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Oznaczenia gamatyki bezkontekstowej G(N,T,P,S): ");
            Console.WriteLine("N - zbiór nieterminali (symbole pomocnicze)");
            Console.WriteLine("T - zbiór terminali (symbole podstawowe)");
            Console.WriteLine("P - zbiór produkcji");
            Console.WriteLine("S - symbol startowy \n");
            
            Console.WriteLine("N = {S, AA, BB, AB}");
            Console.WriteLine("T = {a, b, c, d}");
            Console.WriteLine("P = {S ->AA, S -> BB, S -> AB, ");
            Console.WriteLine("     A->Ac, A->AA, A->ac, B->Bb, B->BB, B->bd}");
            Console.WriteLine("symbol starowty: S \n");
            
            S slowo = new S();
            char[] d = slowo.Losuj();
            Console.WriteLine(d);
            Console.WriteLine(slowo.buduj_drzewo(d));

            Console.ReadKey();
        }
    }
}
