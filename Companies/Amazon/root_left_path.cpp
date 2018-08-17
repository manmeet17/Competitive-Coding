//Functional Problem

vector<int>path;

void printPath(const vector<int> &path)
{
    for(auto it : path){
        cout<<it<<" ";
    }
}


void printPaths(Node* root)
{
    path.push_back(root->data);
    if(!root->left && !root->right)
    {
        printPath(path);
        path.pop_back();
        cout<<"#";
        return;
    }
    printPaths(root->left);
    printPaths(root->right);
    path.pop_back();
    if(path.size()<1)
        cout<<endl;
}
