
/* Tree node structure  used in the program
 struct Node
 {
     int data;
     Node* left, *right;
}; */
/* Computes the diameter of binary tree with given root.  */
int m=INT_MIN;
int depth(Node *node)
{
    if(!node)
        return 0;
    int l=depth(node->left);
    int r=depth(node->right);
    if(l+r+1>m) 
        m=l+r+1;
    if(l>r) return l+1;
    return r+1;
}

int diameter(Node* node)
{
    m=INT_MIN;
    depth(node);
    return m;
}
