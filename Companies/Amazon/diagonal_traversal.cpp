void rightTree(Node *root,int hd, map< int,vector<int>>&m)
{
    if(root==NULL)
        return;
    m[hd].push_back(root->data);
    if (root->left)
        rightTree(root->left,hd-1,m);
    if (root->right)
        rightTree(root->right,hd,m);
}


void diagonalPrint(Node *root)
{
    map<int,vector<int> >m;
    int hd=0;
    rightTree(root,hd,m);
    for (auto it=m.rbegin(); it!=m.rend(); it++)
    {
        // cout<<it->first<<endl;
        for (int i=0; i<it->second.size(); ++i)
            cout << it->second[i] << " ";
    }
    
}
