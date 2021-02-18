package com.company;//pracownia 6 zad 2

import java.util.Collection;
import java.util.Iterator;
import java.util.Objects;

public class List<T extends Comparable<? super T>>// jak chcemy porownac typ generyczny T to porownujemy go z innym obiektem który jest nad klasą nad T
        implements Iterable<T>, Collection<T> //Iterable - foreach
{
    static class Element<T>{
        T value;
        Element<T> next;
        Element<T> prev;

        Element(T data) { //konstruktor
            value = data;
            next = null;
            prev = null;
        }
    }

    Element<T> first;
    Element<T> last;
    int size;

    List(){
        first = null;
        last = null;
        size = 0;
    }

    @Override
    public int size(){
        return size;
    }

    @Override
    public boolean isEmpty(){
        if(size == 0)
            return true;
        return false; //if
    }

    @Override
    @SuppressWarnings("unchecked")
    public boolean contains(Object o){ //sprawdza czy jakiś obiekt typu object o nazwie 'o' zawiera sie w liscie
        if (isEmpty()) return false;
        Comparable<? super T> t = (Comparable<? super T>) o; //rzutowanie
        for (T elem : this){
            if (elem == t) return true;
        }
        return false;
    }

    @Override
    public Iterator<T> iterator(){

        return new Iterator<T>(){
            private Element<T> current = first;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                T res = current.value;
                current = current.next;
                return res;
            }
        };
    }

    @Override
    public Object[] toArray(){ //konwertuje liste na tablice
        Object[] tab = new Object[size];
        Element<T> current = first;
        int i = 0;
        while (current != null){
            tab[i] = current.value;
            current = current.next;
            i++;
        }
        return tab;
    }

    @Override
    public <T1> T1[] toArray(T1[] t1s){ //tworzy nowa tablice z kopią listy
        Objects.requireNonNull(t1s); //sprawdza czy t1s jest pusty
        if (size() > t1s.length) return (T1[])toArray();
        int idx = 0;
        for (T every : this ){
            t1s[idx] = (T1)every;
            idx++;
        }

        for (int i = idx; i < t1s.length; i++){
            t1s[i] = null;
        }
        return t1s;
    }

    @Override
    public boolean add(T t) {
        if (first == null){
            Element newelem = new Element(t);
            first = newelem;
            last = newelem;
            first.next = last;
            last.prev = first;
            size = 1  ;
        }
        else if (this.size() == 1){
            Element<T> newelem = new Element(t);
            last = newelem;
            last.prev = first;
            first.next = last;
            size++;
        }
        else{
            Element<T> newelem = new Element(t);
            newelem.prev = last;
            last.next = newelem;
            last = newelem;
            size++;
        }
        return true;
    }

    @Override
    public boolean remove(Object o) {
        if (!contains(o)) return false;
        else{
            Comparable<? super T> t = (Comparable<? super T>) o;
            if (size == 1){
                first.next = null;
                last.prev = null;
                first = null;
                last = null;
                size = 0;
            }
            else if (t == last.value){
                last.prev.next = null;
                last = last.prev;
                size--;
            }
            else if(first.value == t){
                first = first.next;
                size--;
            }
            else{
                Element temp = first;
                Element prev = null;
                while (temp != null){
                    while (temp != null && temp.value != t){
                        prev = temp;
                        temp = temp.next;
                    }
                    if (temp == null) return false;
                    prev.next = temp.next;
                    temp = prev.next;
                    size--;
                }
            }
            return true;
        }
    }

    @Override
    public boolean containsAll(Collection<?> collection){ //kolekcja o niezananym typie
        return collection.stream().allMatch(this::contains); //przekonwertowanie kolekcji na stream
                                                             // (przechwuje wzystki elemetny kolekcji)
    }

    @Override
    public boolean addAll(Collection<? extends T> collection) {
        if (collection.isEmpty()) return false;

        for (T every : collection){
            this.add(every);
        }
        return true;
    }

    @Override
    public boolean removeAll(Collection<?> collection) {
        if (collection.isEmpty()) return false;
        boolean flag = false;
        List<T> copy = new List<>();
        copy.addAll(this);
        //System.out.println("Elementy kolekcji");
        //collection.stream().forEach(System.out::print);
        //System.out.println("Kazdy w koppii:");
        for (T every : copy){
            //System.out.print(every + "...");
            if (collection.stream().anyMatch(e -> e.equals(every))){
                this.remove(every);
                flag = true;
            }
        }
        return flag;
    }

    @Override
    public boolean retainAll(Collection<?> collection){
        if (collection.isEmpty()) return false;
        boolean flag = false;
        List<T> copy = new List<>();
        copy.addAll(this);

        for (T every : copy){
            //System.out.print(every + "...");
            if(!collection.stream().anyMatch(e -> e.equals(every))){
                this.remove(every);
                flag = true;
            }
        }
        return flag;
    }

    @Override
    public void clear() {
        if (size == 0) return;
        first.next = null;
        last.prev = null;
        first = null;
        last = null;
        size = 0;
    }

    @Override
    public String toString(){
        if (size == 0) return "[]";

        StringBuilder result = new StringBuilder("[");
        for (T e: this) {
            result.append(e);
            result.append(", ");
        }
        result.append("\b\b]");
        return result.toString();
    }
}
