namespace Lib.Base
{
    public abstract class Problem
    {
        #region Public Properties.

        public string ProblemName { get; protected set; }
        public string Url { get; private set; }

        #endregion

        #region Constructors.

        public Problem(string problemName, string url)
        {
            this.ProblemName = problemName;
            this.Url = url;
        }

        #endregion

        #region Public Abstract Methods.

        public virtual void Solve()
        {
            System.Console.WriteLine(string.Format(""));
        }

        #endregion
    }
}
