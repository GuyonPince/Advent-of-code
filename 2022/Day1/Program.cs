string path = "calories.txt";
var lines = File.ReadAllLines(path);

int[] maxval = { 0, 0, 0};
int val = 0;

foreach (var line in lines)
{
    if (line == "")
    {
        int maxindex = 0;
        bool found = false;
        for (int i = 0; i < maxval.Length; i++)
        {
            Console.WriteLine(maxval[i] + "=>" + val);
            if (val > maxval[i])
            {
                Console.WriteLine(maxval[i] + "===>" + val + "  -- index " + i);
                maxindex = i;
                found = true;
            }
        }
        if (found) { maxval[maxindex] = val; }
        val = 0;
    }
    else
    {
        int cal = int.Parse(line);
        val += cal;
    }
}

int top3 = 0;
foreach (int x in maxval) 
{ 
    Console.WriteLine(x);
    top3 += x;
}
Console.WriteLine("top3 = " + top3);

//64545
//69434
//69795
//top3 = 203774