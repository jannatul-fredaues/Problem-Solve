#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    int at[n], bt[n], ct[n], tat[n], wt[n], pid[n];

    // Input
    cout << "Enter Arrival Time:\n";
    for (int i = 0; i < n; i++) {
        cin >> at[i];
        pid[i] = i + 1; // process ID
    }

    cout << "Enter Burst Time:\n";
    for (int i = 0; i < n; i++) {
        cin >> bt[i];
    }

    // Sort by Arrival Time (FCFS)
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[i] > at[j]) {
                swap(at[i], at[j]);
                swap(bt[i], bt[j]);
                swap(pid[i], pid[j]);
            }
        }
    }

    // Calculate Completion Time
    ct[0] = at[0] + bt[0];

    for (int i = 1; i < n; i++) {
        if (ct[i - 1] < at[i])
            ct[i] = at[i] + bt[i];   // CPU idle
        else
            ct[i] = ct[i - 1] + bt[i];
    }

    float avgWT = 0, avgTAT = 0;

    cout << "\nProcess\tAT\tBT\tCT\tTAT\tWT\n";
    for (int i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];

        cout << "P" << pid[i] << "\t" << at[i] << "\t" << bt[i]
             << "\t" << ct[i] << "\t" << tat[i] << "\t" << wt[i] << endl;

        avgWT += wt[i];
        avgTAT += tat[i];
    }

    cout << "\nAverage Waiting Time = " << avgWT / n;
    cout << "\nAverage Turnaround Time = " << avgTAT / n;

    // Gantt Chart (order only)
    cout << "\nGantt Chart Order:\n| ";
    for (int i = 0; i < n; i++) {
        cout << "P" << pid[i] << " | ";
    }
    cout << endl;

    return 0;
}