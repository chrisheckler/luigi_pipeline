#!/usr/bin/env python3
# Copytright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

import luigi

class PrintNumbers(luigi.Task):
    n = luigi.IntParameter()

    def requires(self):
        """
        Designates required tasks if any. In this case there is not.
        """
        return []

    def output(self):
        """
        Designates an output source.  A txt file for this instance.
        """
        return luigi.LocalTarget('numbers_up_to_{}.txt'.format(self.n))

    def run():
        """
        The part that is exectuted to accomplish or transform data
        """
        with self.output().open('w') as f:
            for i in range(1, self.n+1):
                f.write("{}\n".format(i))

#class SquareNumbers(luigi.Task):


if __name__=="__main__":
    luigi.run()
