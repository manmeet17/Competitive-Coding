#include <bits/stdc++.h>
using namespace std;
/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
};
bool isBalanced(struct Node *root);
/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct Node* newNode(int data)
{
  struct Node* node = new Node;
  node->data = data;
  node->left = NULL;
  node->right = NULL;
  return(node);
}
/* Driver program to test size function*/
int main()
{
  int t;
  scanf("%d
", &t);
  while (t--)
  {
     map<int, Node*> m;
     int n;
     scanf("%d",&n);
     struct Node *root = NULL;
     struct Node *child;
     while (n--)
     {
        Node *parent;
        char lr;
        int n1, n2;
        scanf("%d %d %c", &n1, &n2, &lr);
        if (m.find(n1) == m.end())
        {
           parent = newNode(n1);
           m[n1] = parent;
           if (root == NULL)
             root = parent;
        }
        else
           parent = m[n1];
        child = newNode(n2);
        if (lr == 'L')
          parent->left = child;
        else
          parent->right = child;
        m[n2]  = child;
     }
     cout << isBalanced(root) << endl;
  }
  return 0;
}


/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* A binary tree node structure
struct Node {
    int data;
    Node* left, * right;
}; */
// This function should return tree if passed  tree 
// is balanced, else false.  Time complexity should
//  be O(n) where n is number of nodes in tree


int height(Node *root)
{
    if(!root) return 0;
    int ldepth=height(root->left);
    int rdepth=height(root->right);
    if(ldepth>rdepth)
        return ldepth+1;
    return rdepth+1;
}


bool isBalanced(Node *root)
{
    //  Your Code here
    if(!root)
        return true;
    int l=height(root->left);
    int r=height(root->right);
    if(abs(l-r)>1)
        return false;
    if(isBalanced(root->left) && isBalanced(root->right))
        return true;
    return false;
}

