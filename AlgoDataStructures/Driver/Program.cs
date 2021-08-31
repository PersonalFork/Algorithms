
using System;

using DataStructures.Arrays;
using DataStructures.Sorting;

namespace Driver
{
    internal class Program
    {
        private static void Main()
        {
            object[] array = { "1", "2", "3", "4", "5", "6", "7" };
            //array.Print();

            //#region Rotate By N

            //int n = 2;
            //Console.WriteLine("\nRotating by " + n);
            //array.RotateByN(n, RotateApproach.TempStorage);
            //Console.Read();

            //#endregion

            int[] unsortedArray = { 5, 1, 7, 6, 6, 3 };
            unsortedArray.Print();
            MergeSort.Sort(unsortedArray);
            unsortedArray.Print();

            Console.Read();
        }
    }
}
