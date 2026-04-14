#include <iostream>
using namespace std;

int main() {
    int n, frames;

    cout << "Enter number of pages: ";
    cin >> n;

    int pages[n];
    cout << "Enter page reference string:\n";
    for (int i = 0; i < n; i++)
        cin >> pages[i];

    cout << "Enter number of frames: ";
    cin >> frames;

    int frame[frames], recent[frames];
    int page_faults = 0;

    // Initialize frames
    for (int i = 0; i < frames; i++) {
        frame[i] = -1;
        recent[i] = -1;
    }

    for (int i = 0; i < n; i++) {
        int found = -1;

        // Check if page already exists
        for (int j = 0; j < frames; j++) {
            if (frame[j] == pages[i]) {
                found = j;
                break;
            }
        }

        if (found != -1) {
            // Page hit → update recent use
            recent[found] = i;
        } else {
            // Page fault
            int pos = 0;

            // Find least recently used
            for (int j = 1; j < frames; j++) {
                if (recent[j] < recent[pos]) {
                    pos = j;
                }
            }

            frame[pos] = pages[i];
            recent[pos] = i;
            page_faults++;
        }

        // Print frame status (for visualization)
        cout << "Step " << i+1 << ": ";
        for (int j = 0; j < frames; j++) {
            if (frame[j] == -1)
                cout << "- ";
            else
                cout << frame[j] << " ";
        }
        cout << endl;
    }

    cout << "\nTotal Page Faults = " << page_faults << endl;

    return 0;
}