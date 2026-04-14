#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    int at[n], bt[n], ct[n], tat[n], wt[n];
    bool done[n] = {false};

    cout << "Enter Arrival Time:\n";
    for (int i = 0; i < n; i++)
        cin >> at[i];

    cout << "Enter Burst Time:\n";
    for (int i = 0; i < n; i++)
        cin >> bt[i];

    int completed = 0, time = 0;

    while (completed < n) {
        int idx = -1, min_bt = 1e9;

        for (int i = 0; i < n; i++) {
            if (at[i] <= time && !done[i] && bt[i] < min_bt) {
                min_bt = bt[i];
                idx = i;
            }
        }

        if (idx == -1) {
            time++;
        } else {
            time += bt[idx];
            ct[idx] = time;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];

            done[idx] = true;
            completed++;
        }
    }

    float avgWT = 0, avgTAT = 0;

    cout << "\nProcess\tAT\tBT\tCT\tTAT\tWT\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << i+1 << "\t" << at[i] << "\t" << bt[i]
             << "\t" << ct[i] << "\t" << tat[i] << "\t" << wt[i] << endl;

        avgWT += wt[i];
        avgTAT += tat[i];
    }

    cout << "\nAverage Waiting Time = " << avgWT / n;
    cout << "\nAverage Turnaround Time = " << avgTAT / n;

    return 0;
}