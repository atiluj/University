package com.company; //Julita Osman 314323 pracownia 6 zad 5
import java.util.Arrays;

class MergeSort extends Thread
{
    public int[] array;

    public MergeSort(int[] a) //konstruktor
    {
        array = a;
    }

    public void mergeSort(int[] array) throws InterruptedException{
        int length = array.length;
        if (length > 1){
            int mid = length/2;
            int[] left = Arrays.copyOfRange(array, 0, mid);
            int[] right = Arrays.copyOfRange(array, mid, length);

            MergeSort sort1 = new MergeSort(left);
            MergeSort sort2 = new MergeSort(right);

            sort1.start();
            sort2.start();

            sort1.join();
            sort2.join();

            merge(array, left, right);
        }
    }
    private void merge(int[] result, int[] left, int[] right)
    {
        int i = 0, j = 0, k = 0;
        int len1 = left.length;
        int len2 = right.length;

        while (i < len1 && j < len2)
        {
            if (left[i] < right[j])
                result[k++] = left[i++];
            else
                result[k++] = right[j++];
        }

        while (i < len1)
            result[k++] = left[i++];
        while (j < len2)
            result[k++] = right[j++];
    }
    @Override
    public void run(){
        try {
            mergeSort(array);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}