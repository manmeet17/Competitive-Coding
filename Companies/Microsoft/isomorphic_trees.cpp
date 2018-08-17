bool isIsomorphic(Node *root1,Node *root2)
{
    if(!root1 && !root2)
        return true;
    if((!root1 || !root2))
        return false;
    if(root1->data!=root2->data)
        return false;

    bool lref=isIsomorphic(root1->left,root2->left);
    bool rref=isIsomorphic(root1->right,root2->right);
    bool lmirror=isIsomorphic(root1->left,root2->right);
    bool rmirror=isIsomorphic(root1->right,root2->left);
    
    return((lref && rref) || (lmirror && rmirror));
}
