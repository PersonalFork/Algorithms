using DataStructures.Arrays;

using System;

namespace Driver
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            string[] array = new string[] { "1", "2", "3", "4", "5", "6", "7" };
            array.Print();

            #region Rotate By N

            int n = 2;
            Console.WriteLine("\nRotating by " + n);
            array.RotateByN(n, RotateApproach.TempStorage);
            Console.Read();

            #endregion
        }
    }
}
