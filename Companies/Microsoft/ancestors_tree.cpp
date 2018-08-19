bool printPath(struct Node *root,int target)
{
    if(root==NULL)
        return false;
    if(root->data==target)
        return true;
    if(printPath(root->left,target) || printPath(root->right,target)){
        cout<<root->data<<" ";
        return true;   
    }
    return false;
}
// Function should print all the ancestor of the target node
bool printAncestors(struct Node *root, int target)
{
    printPath(root,target);
    cout<<endl;
}
