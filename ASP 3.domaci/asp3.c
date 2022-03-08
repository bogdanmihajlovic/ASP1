
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int val;
	int len;
	int *path;
	int visited[100];
	struct Node* next;

}Node;

void menu();
void enterField(int**, int**, int*, int*);
void deleteNode(int**, int**, int, int*, int*);
void deleteEdge(int**, int**, int node1, int node2, int* lenEdges, int* lenIndices);
void addEdge(int**, int**, int, int, int*, int*);
void addNode(int**, int**, int, int*, int n1, int*, int n2, int*, int*);
struct Node* insert(Node* head, int value);
int isEmpty(Node* head);
int deleteQ(Node** head);
int minPathFirst(int* edges, int* indices, int start, int check, int lenEdges, int lenIndices);
int minPathSecond(int* edges, int* indices, int lenEdges, int lenIndices);
void printPath(Node* head);
struct Node* insertArray(Node* head,int *arr,int len,int new,int,int*);
Node* deleteArray(Node** head);
void printAllPath(int* edges, int* indices, int* lenIndices, int* lenEdges);

int main() {
	int n, * edges = NULL, * indices = NULL, numNodes, temp, numEdges;
	enterField(&edges, &indices, &numNodes, &numEdges);
	printAllPath(edges,indices,&numNodes,&numEdges);
	return 0;
	//n =   minPathFirst(edges,indices,0,1,numEdges,numNodes);
	//printf("Najkrace rastojanje 1 je %d\n",n);
	//n =   minPathSecond(edges,indices,numEdges,numNodes);
	//printf("Najkrace rastojanje 2 je %d",n);

	//edges = addNode(edges,indices,5,list1,2,list2,1,numEdgesptr,numNodesptr);
	//edges = addEdge(edges,indices,5,1,numEdgesptr,numNodesptr);
	struct Node* head = NULL;
	head = insert(head, 10);
	int list1[10], list2[10], len1, len2;

	while (1) {
		menu();
		scanf("%d", &n);
		putchar('\n');
		switch (n) {
			case 1:
				enterField(&edges, &indices, &numNodes, &numEdges);
				break;
			case 2:
				len1 = 0, len2 = 0;
				printf("Upisite na koja polja ce pokazivati novo polje: ");
				while (1) {
					scanf("%d", &temp);
					if (temp == -1) break;
					list1[len1++] = temp;
				}
				//getchar();
				printf("\nUpisite koja polja ce pokazivati na novo polje: ");
				while (1) {
					scanf("%d", &temp);
					if (temp == -1) break;
					list2[len2++] = temp;
				}
				addNode(&edges, &indices, numNodes, list1, len1, list2, len2, &numEdges, &numNodes);
				putchar('\n');
				break;
			case 3:
				printf("Unesite koje polje hocete da obriste: ");
				scanf("%d", &temp);
				if (numNodes < temp) {
					printf("Uneto polje ne postoji\n");
					continue;
				}
				if (indices[temp - 1] == -1) {
					printf("Polje je vec obrisano\n");
					continue;
				}
				deleteNode(&edges, &indices, temp, &numEdges, &numNodes);
				putchar('\n');
				break;
			case 4:
				printf("Unesite polja izmedju kojih hocete da dodate vezu: ");
				scanf("%d %d ", &n, &temp);
				addEdge(&edges, &indices, n, temp, &numEdges, &numNodes);
				putchar('\n');
				break;
			case 5:
				printf("Unesite polja izmedju kojih hocete da obrisete vezu: ");
				scanf("%d %d ", &n, &temp);
				deleteEdge(&edges, &indices, n, temp, &numEdges, &numNodes);
				putchar('\n');
				break;
			case 6:
				n = minPathFirst(edges, indices, 0, 1, numEdges, numNodes);
				temp = minPathSecond(edges, indices, numEdges, numNodes);
				if (!n && !temp) {
					printf("Ni jedan igrac ne moze da dodje do cilja!\n");
				}
				else if (!temp) {
					printf("Drugi igrac je izgubio jer nema puta do cilja!\n");
				}
				else if (!n) {
					printf("Prvi igrac je izgubio jer nema puta do cilja!\n");
				}
				else if (n && temp > n) {
					printf("Prvi igrac je pobedio\n");
				}
				else if (temp && temp < n) {
					printf("Drugi igrac je pobedio\n");
				}
				else printf("Izjednaceno je\n");
				printf("Prvom igracu treba %d poteza do cilja\nDrugom igracu treba %d poteza do cilja\n", n, temp);

				break;
			case 7:

				break;
			case 8:
				return 0;
			default:
				printf("Izaberite ponovo!\n");
				continue;

		}
	}

}

void menu() {

	printf("\n1. Unesite odgovarajuce polje\n");
	printf("2. Dodajte cvor\n");
	printf("3. Obrisite cvor\n");
	printf("4. Dodajte granu\n");
	printf("5. Obrisite granu\n");
	printf("6. Odredite pobednika\n");
	printf("7. Prikaz svih minimalnih puteva\n");
	printf("8. Izlaz\n");
	printf("Izaberine opciju: ");
}
void enterField(int** edges, int** indices, int* n, int* lenEdges) {


	printf("Unesi broj polja: ");
	scanf("%d", n);

	putchar('\n');
	int temp = *n * (*n -1);

	//realokacija prostora
	*indices = malloc((*n + 1)* sizeof(int));
	*edges = malloc(temp * sizeof(int));

	if (edges == NULL || indices == NULL) {
		printf("MEM_GRESKA\n");
		exit(0);
	}
	int* oldEdges = *edges;
	int j = 0;
	for (int i = 0; i < *n; i++) {
		(*indices)[i] = j;
		printf("Unesite sa kojim poljima ce biti povezano polje %d:\n(Kraj unosa se oznacava sa -1)\n", i + 1);
		for (;;) {
			scanf("%d", &temp);
			if (temp == -1) break;
			(*edges)[j++] = temp;
		}
	}

	(*indices)[*n] = j;
	//*edges = realloc(oldEdges,j*sizeof(int));
	if (!*edges) {
		printf("MEM_GRESKA\n");
		exit(0);
	}
	printf("Edges: ");

	for (int l = 0; l < j; l++) {
		printf("%d%c", (*edges)[l], (l != j - 1) ? ' ' : '\n');
	}
	printf("Indices: ");
	for (int l = 0; l <= *n; l++) {
		printf("%d%c", (*indices)[l], (l != *n) ? ' ' : '\n');
	}
	*lenEdges = j;
}
void deleteNode(int** edges, int** indices, int node, int* lenEdges, int* lenIndices) {
	if (indices == NULL) {
		printf("Polje je prazno\n");
		return;
	}
	int startIndex = (*indices)[node - 1], endIndex = (*indices)[node];

	//prvo brisemo iz edgesa cvorove na koje pokazuje cvor koji brisemo
	for (int i = startIndex; i < endIndex; i++) {
		for (int j = startIndex + 1; j < *lenEdges; j++) (*edges)[j - 1] = (*edges)[j];
		*lenEdges = *lenEdges - 1;
	}
	//markiramo cvor koji brisemo
	(*indices)[node - 1] = -1;

	for (int i = node; i <= *lenIndices; i++) {
		(*indices)[i] = (*indices)[i] - (endIndex - startIndex);
	}
	//brisemo iz edgesa cvor na koji pokazuju ostali cvorovi
	for (int i = 0; i < *lenEdges; i++) {
		if ((*edges)[i] == node) {
			//brisem ga iz edges
			for (int j = i + 1; j < *lenEdges; j++) edges[j - 1] = edges[j];
			//u indices pomeram moram da promenim granicu indeksa
			for (int j = 1; j <= *lenIndices; j++) {
				if ((*indices)[j] > i) (*indices)[j]--;
			}
			i--;
			*lenEdges = *lenEdges - 1;
		}
	}

}
void deleteEdge(int** edges, int** indices, int node1, int node2, int* lenEdges, int* lenIndices) {
	if (indices == NULL) {
		printf("Polje je prazno\n");
		return;
	}
	int startIndex = indices[0][node1 - 1], endIndex = indices[0][node1];
	int temp = -1;
	for (int i = startIndex; i < endIndex; i++) {
		if (edges[0][i] == node2) temp = i;
	}
	if (temp == -1) {
		printf("Ovo polje ne pokazuje na polje koje ste izabrali\n");
		//return edges;
	}
	for (int i = 1; i <= *lenIndices; i++) {
		if (indices[0][i] > temp) indices[0][i]--;
	}
	for (int i = temp + 1; i < *lenEdges; i++) edges[0][i - 1] = edges[0][i];
	*lenEdges -= 1;

}
void addEdge(int** edges, int** indices, int node1, int node2, int* lenEdges, int* lenIndices) {
	if (indices == NULL) {
		printf("Polje je prazno\n");
		return;
	}
	int startIndex = indices[0][node1 - 1], endIndex = indices[0][node1];
	int temp = -1;
	for (int i = startIndex; i < endIndex; i++) {
		if (edges[0][i] == node2) temp = i;
	}
	if (temp != -1) {
		printf("vec postoji veza\n");
		//return edges;
	}

	temp = startIndex;
	while (temp < endIndex && edges[0][temp] < node2) temp++;

	for (int i = *lenEdges; i > temp; i--) edges[0][i] = edges[0][i - 1];
	edges[0][temp] = node2;
	*lenEdges += 1;
	for (int i = 1; i <= *lenIndices; i++) {
		if (indices[0][i] > temp) indices[0][i]++;
	}

	//return edges;
}
void addNode(int** edges, int** indices, int node, int* list1, int n1, int* list2, int n2, int* lenEdges, int* lenIndices) {
	if (indices == NULL) {
		printf("Polje je prazno\n");
		return;
	}
	//provera da li u indices postoji neki cvor koji smo obrisali
	int temp = 0;
	for (int i = 0; i < *lenIndices; i++) {
		if ((*indices)[i] == -1) {
			temp = i;
			break;
		}
	}
	if (temp == 0) {
		*indices = realloc(*indices, (*lenIndices + 1) * sizeof(int));
		if (!*indices) {
			printf("MEM_GRESKA\n");
			exit(0);
		}
		for (int i = 0; i < n1; i++) {
			(*edges)[*lenEdges + i] = list1[i];
		}
		*lenEdges += n1;
		*lenIndices += 1;
		indices[*lenIndices] = indices[*lenIndices - 1] + n1;
		for (int j = 0; j < n2; j++) {
			//startIndex = indices[list2[j] - 1];
			int endIndex = (*indices)[list2[j]];


			for (int i = *lenEdges; i > endIndex; i--) edges[i] = edges[i - 1];
			(*edges)[endIndex] = node;
			*lenEdges += 1;
			for (int i = 1; i <= *lenIndices; i++) {
				if (indices[0][i] > endIndex) indices[0][i]++;
			}

		}

	}
	else {
		int startIndex = indices[0][temp + 1], endIndex, t;
		for (int i = n1 - 1; i >= 0; i--) {
			//list1[i] stavljamo
			for (int j = *lenEdges; j > startIndex; j--) edges[j] = edges[j - 1];
			edges[0][startIndex] = list1[i];
			*lenEdges += 1;
		}
		indices[0][temp] = startIndex;
		for (int i = temp + 1; i <= *lenIndices; i++) indices[i] += n1;

		for (int j = 0; j < n2; j++) {
			startIndex = indices[0][list2[j] - 1];
			endIndex = indices[0][list2[j]];
			t = startIndex;
			while (t < endIndex && edges[0][t] < temp + 1) t++;

			for (int i = *lenEdges; i > t; i--) edges[0][i] = edges[0][i - 1];
			edges[0][t] = temp + 1;
			*lenEdges += 1;
			for (int i = 1; i <= *lenIndices; i++) {
				if (indices[0][i] > t) indices[0][i]++;
			}
		}
	}
}
struct Node* insert(Node* head, int value) {
	Node* new = malloc(sizeof(Node));
	if (!new) exit(0);
	new->val = value;
	new->next = NULL;
	if (!head) {
		head = new;
		return head;
	}
	Node* p = head;
	while (p->next) p = p->next;
	p->next = new;
	return head;
}
int deleteQ(Node** head) {
	int t;
	Node* p = *head, * q = *head;
	while (p->next) p = p->next;
	t = p->val;
	if (p == *head) {
		free(*head);
		*head = NULL;
		return t;
	}
	while (q->next != p) q = q->next;
	q->next = NULL;
	free(p);
	return t;
}
int isEmpty(Node* head) {
	if (head) return 0;
	return 1;
}
int minPathFirst(int* edges, int* indices, int start, int check, int lenEdges, int lenIndices) {

	Node* q = NULL;
	int *visit,*level,*path;
	//int level[lenIndices], visit[lenIndices];
	int v, u, j = lenIndices - 1;

	level = malloc((lenIndices )* sizeof(int) );
	visit = malloc( (lenIndices + 1)* sizeof(int) );
	//if( !visit || !level){
	//	printf("MEM_GRESKA\n");
	//	exit(0);
	//}

	int startI, endI;
	for (int i = 0; i < lenIndices; i++) { visit[i] = 0, level[i] = 0; }
	visit[0] = 1;
	q = insert(q, start);
	while (!isEmpty(q)) {
		v = deleteQ(&q);
		startI = indices[v];
		endI = indices[v + 1];
		for (int i = startI; i < endI; i++) {
			u = edges[i] - 1;
			if (!visit[u]) {
				visit[u] = 1;
				level[u] = level[v] + 1;
				if (u == j) {
					u = level[u];
					//int path[u];
					path = malloc(u * sizeof(int));
					for (int l = 0; l < lenIndices; l++) {
						if (visit[l]) {
							path[level[l]] = l + 1;
						}
					}
					if (check) {
						for (int l = 0; l < u; l++) printf("%d->", path[l]);
						printf("%d\n", j + 1);
					}
					return u;
				}
				q = insert(q, u);
			}
		}
	}
	return level[j];
}
int minPathSecond(int* edges, int* indices, int lenEdges, int lenIndices) {

	Node* q = NULL, * path = NULL;
	int *visit;
	//int visit[lenIndices];
	int potez = 1, v, u, j = lenIndices - 1;
	//level = malloc((lenIndices )* sizeof(int) );
	visit = malloc( (lenIndices + 1)* sizeof(int) );

	//if( !visit || !level){
	//	printf("MEM_GRESKA\n");
	//	exit(0);
	//}

	int startI, endI;
	for (int i = 0; i < lenIndices; i++) visit[i] = 0;
	visit[0] = 1;

	q = insert(q, 0);

	while (!isEmpty(q)) {
		v = deleteQ(&q);
		path = insert(path, v + 1);
		startI = indices[v];
		endI = indices[v + 1];
		if (potez % 2) {
			for (int i = startI; i < endI; i++) {
				u = edges[i] - 1;
				if (!visit[u]) {
					visit[u] = 1;
					if (u == j) {
						//stampaj
						printPath(path);
						printf("%d\n", j + 1);
						return potez;

					}
					q = insert(q, u);
				}
			}

		}
		else {
			for (int i = startI; i < endI; i++) {
				u = edges[i] - 1;
				if (!visit[u] && u != j) {
					visit[u] = 1;
					q = insert(q, u);
				}
			}
			if (isEmpty(q)) {
				for (int i = 0; i < lenIndices; i++) visit[i] = 0;
				//trazimo sina sa najmanjoj putanjom do poslednjeg cvora
				//dodamo ga u red
				int cvor = edges[startI], curr, minPath = lenIndices;
				for (int i = startI; i < endI; i++) {
					curr = minPathFirst(edges, indices, edges[i] - 1, 0, lenEdges, lenIndices);
					if (curr < minPath) {
						minPath = curr;
						cvor = edges[i] - 1;
					}
				}
				q = insert(q, cvor);
			}
			v = deleteQ(&q);
			path = insert(path, v + 1);
			startI = indices[v];
			endI = indices[v + 1];
			for (int i = startI; i < endI; i++) {
				u = edges[i] - 1;
				if (!visit[u]) {
					visit[u] = 1;
					if (u == j) {
						//stampaj
						printPath(path);
						printf("%d\n", j + 1);
						return potez;
					}
					q = insert(q, u);
				}
			}
		}
		potez++;
	}
	return 0;
}
void printPath(Node* head) {
	Node* p = head;
	while (p) {
		printf("%d->", p->val);
		p = p->next;
	}
}
void printAllPath(int* edges, int* indices, int* lenIndices, int* lenEdges){
	//int visited[20];
	//for(int i = 0;i < *lenIndices;i++) visited[i] = 0;
	int min = minPathFirst(edges,indices,0,0,*lenEdges,*lenIndices) + 1;

	Node* q = NULL;
	int end = *lenIndices - 1;
	int temp1[15] = {0};
	struct Node *temp;
	q = insertArray(q,temp1,0,0,*lenIndices,temp1);
	//visited[0] = 1;
	int node,startI, endI,u;
	while(!isEmpty(q)){
		temp = deleteArray(&q);
		node = temp->path[temp->len - 1];

		if(node == end && temp->len == min){
			//printf
			for(int i = 0; i < temp->len - 1;i++) printf("%d->",temp->path[i] + 1);
			printf("%d\n",node + 1);
		}
		startI = indices[node];
		endI = indices[node + 1];
		for(int i = startI;i < endI;i++){
			u = edges[i] - 1;
			if(!temp->visited[u]){
				temp->visited[u] = 1;
				  q = insertArray(q,temp->path,temp->len,u,*lenIndices,temp->visited);
			}
		}
	}

}
struct Node* insertArray(Node* head,int *arr,int len,int el,int lenIndices,int *vis){

	Node* new = malloc(sizeof(Node));
	new->path = malloc((len + 1)*sizeof(int));
	new->next = NULL;
	new->len = len + 1;

	for(int i = 0;i < len;i++){
		new->path[i] = arr[i];
	}
	new->path[len] = el;
	for(int i = 0;i < lenIndices;i++) {
		new->visited[i] = vis[i];
	}

	new->visited[el] = 1;
	if(!head){
		head = new;
		head->next = NULL;
		//head->path = malloc((len + 1)*sizeof(int));
		return head;
	}
	Node* p = head;
	while(p->next) p = p->next;
	p->next = new;
	return head;
}

Node* deleteArray(Node** head){
	Node* p = *head,*q = *head;
	//while(p->next) p = p->next;
	if (!p->next) {
		*head = NULL;
		return p;
	}
	//while (q->next != p) q = q->next;
	*head = (*head)->next;
	return p;
}




/*
5
2 3 -1
3 5 -1
2 4 -1
2 5 -1
2 -1

6
2 -1
4 6 -1
1 6 -1
5 -1
3 -1
5 -1

4
2 3 -1
3 -1
4 -1
-1

6
2 4 -1
4 6 -1
1 6 -1
5 6 -1
3 -1
5 -1

//rekonstuisem sve puteve za sanju
//sredim brisanje cvorova i dodavanje cvorova
//sredim memoriju
*/